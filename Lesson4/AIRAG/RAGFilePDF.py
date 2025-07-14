from langchain_community.document_loaders import PyPDFLoader
from langchain_community.vectorstores import FAISS
from langchain_ollama.embeddings import OllamaEmbeddings
from langchain_ollama.llms import OllamaLLM
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.chains import RetrievalQA

# Step 1: Load the PDF
pdf_path = "data/Nmap Host Discovery.pdf"
loader = PyPDFLoader(pdf_path)
raw_docs = loader.load()

# Step 2: Split into chunks with overlap (to improve context retention)
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=1200,  # Increased for better context
    chunk_overlap=300,  # Increased overlap
    separators=["\n\n", "\n", " ", ""],
    length_function=len,)
documents = text_splitter.split_documents(raw_docs)

# Step 3: Embed documents using nomic-embed-text
embedding = OllamaEmbeddings(model="nomic-embed-text")
vectorstore = FAISS.from_documents(documents, embedding)

# Step 4: Build retriever with better configuration
retriever = vectorstore.as_retriever()

# Step 5: Load a stronger LLM (recommend mistral for accuracy)
llm = OllamaLLM(model="llama3.1:8b")  # You can also try: gemma3, llama3


# Step 6: Build RAG chain with source tracking
qa_chain = RetrievalQA.from_chain_type(
    llm=llm,
    chain_type="stuff",
    retriever=retriever,
    return_source_documents=True
)

print("RAG System Ready! Type your questions (or 'exit' to quit)")

while True:
    query = input("> ").strip()
    if query.strip().lower() == "exit":
        print("Bye Bye 👋")
        break
    response = qa_chain.invoke({"query": query})
    print("\n📘 Result Answer: \n", response["result"], "\n")
    print("📄 Source from File: \n", response["source_documents"][0].page_content[:500], "...\n")




