import streamlit as st
import pandas as pd
import numpy as np
import faiss
from sentence_transformers import SentenceTransformer

# 1. Load data with description vectors
@st.cache_resource
def load_data():
    df = pd.read_pickle("products_with_vectors.pkl")  
    vectors = np.vstack(df["DescriptionVector"].values).astype("float32")
    return df, vectors

# 2. Build FAISS index
def build_index(vectors):
    dim = vectors.shape[1]
    index = faiss.IndexFlatL2(dim)
    index.add(vectors)
    return index

# 3. Perform semantic search
def semantic_search(query, model, index, df, top_k=5):
    q_vec = model.encode([query]).astype("float32")
    D, I = index.search(q_vec, top_k)
    results = df.iloc[I[0]].copy()
    results["Score"] = D[0]
    return results

# 4. Load model + UI
def main():
    st.set_page_config(page_title="🛍 Myntra Semantic Search", layout="centered")
    st.title("🛒 Semantic Search in Myntra Catalog")

    df, vectors = load_data()
    index = build_index(vectors)
    model = SentenceTransformer("all-mpnet-base-v2")

    query = st.text_input("Describe what you're looking for (e.g., 'blue cotton kurta for women')")

    if query:
        results = semantic_search(query, model, index, df)
        st.write("### 🔍 Top Matching Products:")
        for _, row in results.iterrows():
            st.subheader(row["ProductName"])
            st.write(f"📝 {row['Description']}")
            st.write(f"🎨 Color: {row['PrimaryColor']} | 💰 ₹{row['Price (INR)']}")
            st.write(f"📈 Score: {row['Score']:.2f}")
            st.markdown("---")

if __name__ == "__main__":
    main()
