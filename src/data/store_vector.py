from pinecone import Pinecone, ServerlessSpec

pc = Pinecone(api_key="c8d576ac-1187-4b08-adda-76f68e781913")

index_name = "docs-quickstart-index"

pc.create_index(
    name=index_name,
    dimension=8,
    metric="cosine",
    spec=ServerlessSpec(
        cloud='aws',
        region='us-east-1'
    )
)

