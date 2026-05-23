import os
from langchain_mistralai import MistralAIEmbeddings
from langchain_community.vectorstores import FAISS
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_core.tools import Tool
from langchain_core.documents import Document

class SalesRAGManager:
    def __init__(self, docs_dir="docs_rag", index_dir="faiss_index"):
        """
        Inicializa el gestor RAG.
        :param docs_dir: Directorio donde el usuario coloca archivos de conocimiento (.txt, .md).
        :param index_dir: Directorio donde se guardará localmente el índice de FAISS.
        """
        self.docs_dir = docs_dir
        self.index_dir = index_dir
        
        # 1. Configurar embeddings de Mistral (requiere MISTRAL_API_KEY en variables de entorno)
        self.embeddings = MistralAIEmbeddings(model="mistral-embed")
        self.vectorstore = None

    def indexar_base_conocimiento(self, force_rebuild=False):
        """
        Indexa los documentos en la base de conocimiento y los guarda en un índice FAISS local.
        Si ya existe el índice local, lo carga automáticamente para no consumir tokens de la API.
        """
        # Si ya existe el índice y no se fuerza reconstrucción, lo cargamos directamente
        if os.path.exists(self.index_dir) and not force_rebuild:
            print(f"📦 Cargando índice RAG existente desde '{self.index_dir}'...")
            # FAISS requiere allow_dangerous_deserialization=True para cargar archivos guardados localmente
            self.vectorstore = FAISS.load_local(
                self.index_dir, 
                self.embeddings, 
                allow_dangerous_deserialization=True
            )
            print("✅ RAG cargado exitosamente.")
            return

        print("🔍 Creando base de conocimiento RAG desde cero...")
        documents = []

        # Intentar cargar referencia_ventas.md directamente si existe en el directorio actual
        if os.path.exists("referencia_ventas.md"):
            try:
                with open("referencia_ventas.md", "r", encoding="utf-8") as f:
                    content = f.read()
                doc = Document(page_content=content, metadata={"source": "referencia_ventas.md"})
                documents.append(doc)
                print("📖 [OK] 'referencia_ventas.md' cargado desde la raíz del proyecto.")
            except Exception as e:
                print(f"⚠️ Error cargando 'referencia_ventas.md' en raíz: {e}")

        # Intentar cargar documentos desde la carpeta docs_dir
        if os.path.exists(self.docs_dir):
            files = [f for f in os.listdir(self.docs_dir) if f.endswith((".md", ".txt"))]
            for filename in files:
                filepath = os.path.join(self.docs_dir, filename)
                try:
                    with open(filepath, "r", encoding="utf-8") as f:
                        content = f.read()
                    doc = Document(page_content=content, metadata={"source": filename})
                    documents.append(doc)
                    print(f"📖 [OK] '{filename}' cargado desde '{self.docs_dir}'.")
                except Exception as e:
                    print(f"⚠️ Error cargando '{filename}': {e}")
        else:
            # Crear la carpeta de documentos por si el usuario quiere usarla después
            os.makedirs(self.docs_dir, exist_ok=True)

        if not documents:
            # Documento de respaldo mínimo por si no hay archivos
            print("⚠️ No se encontraron documentos. Creando un documento base por defecto.")
            documents.append(Document(
                page_content="Mistral Sales Agent. Base de conocimientos vacía. Coloca archivos .md o .txt en 'docs_rag/' o 'referencia_ventas.md' en la raíz.",
                metadata={"source": "default.txt"}
            ))

        # 2. Dividir documentos en fragmentos (Chunking)
        splitter = RecursiveCharacterTextSplitter(
            chunk_size=600,
            chunk_overlap=60,
            separators=["\n\n", "\n", ". ", " ", ""]
        )
        chunks = splitter.split_documents(documents)
        print(f"✂️ Documentos divididos en {len(chunks)} fragmentos (chunks).")

        # 3. Generar embeddings e indexar en base vectorial FAISS
        print("🧠 Generando embeddings y guardando índice vectorial...")
        self.vectorstore = FAISS.from_documents(chunks, self.embeddings)
        
        # Guardar localmente
        self.vectorstore.save_local(self.index_dir)
        print(f"💾 Índice guardado exitosamente en '{self.index_dir}/'.")

    def buscar(self, query: str, k: int = 3) -> str:
        """
        Realiza una búsqueda semántica y devuelve el contexto estructurado.
        """
        if not self.vectorstore:
            raise ValueError("El RAG no ha sido indexado. Llama a indexar_base_conocimiento() primero.")
        
        results = self.vectorstore.similarity_search(query, k=k)
        if not results:
            return "No se encontró información relevante en los documentos de referencia."
        
        contexto = []
        for i, doc in enumerate(results, 1):
            source = doc.metadata.get("source", "desconocido")
            contexto.append(f"--- Fragmento {i} (Fuente: {source}) ---\n{doc.page_content}")
            
        return "\n\n".join(contexto)

    def obtener_herramienta_rag(self) -> Tool:
        """
        Devuelve un objeto Tool de LangChain listo para agregarse a la lista 'tools' del agente.
        """
        return Tool(
            name="buscar_referencia_ventas",
            func=self.buscar,
            description=(
                "Útil para responder preguntas cualitativas de negocio. "
                "Úsala cuando te pregunten sobre categorías de productos, definiciones de tamaño de deals "
                "(small/medium/large), políticas de envío, listas de países/ciudades por territorio o preguntas frecuentes."
            )
        )
