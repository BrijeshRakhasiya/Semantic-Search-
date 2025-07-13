# 🛍️ Semantic Search on Myntra Product Catalog using FAISS

This project demonstrates a real-world **semantic product search engine** for the **Myntra fashion catalog** using **FAISS** and **Sentence Transformers**. Users can input natural language queries like _"blue cotton kurti for women"_ and get semantically relevant results — regardless of exact keyword match.

---

## 📌 Project Overview

🔍 **Problem**: Traditional keyword-based search engines return poor results for descriptive or vague queries.

💡 **Solution**: Use **semantic search** via **Sentence-BERT** embeddings and **FAISS indexing**, so that results are based on **meaning**, not just keywords.

---

## 🧠 What is Semantic Search? (Inspired by Google's Hummingbird Algorithm)

In 2013, Google introduced the **Hummingbird algorithm** to improve how it understands the **intent behind queries** rather than just matching individual keywords.

> Instead of matching "blue kurti" literally, it understands the meaning of _"a traditional cotton dress in blue for women"_ and fetches results accordingly.

Semantic search uses:
- **Natural Language Processing (NLP)**
- **Text Embeddings** (using transformers)
- **Vector similarity search** (FAISS)

This approach powers real-world search engines like:
- Google
- Amazon product search
- Netflix/Spotify recommendations

---

## 📂 Dataset

- **Raw File**: `myntra_products_catalog.csv`
- **Processed File**: `products_with_vectors.pkl` (includes 768-dim sentence embeddings)

Each product includes:
- `ProductName`
- `Description`
- `PrimaryColor`
- `Gender`
- `Price (INR)`
- `DescriptionVector`

---

## 🚀 Features

- 🔎 Search fashion products using natural language
- 🧠 Generates semantic vectors using Sentence-BERT (`all-mpnet-base-v2`)
- ⚡ Fast real-time product search with **FAISS**
- 🎨 Interactive UI built with **Streamlit**
- ✅ Auto-generates and caches embeddings if missing

---

## ⚙️ How It Works

1. 📝 Descriptions are generated from catalog fields.
2. 🔡 Sentence-BERT converts each description to a 768-dim vector.
3. 🧠 FAISS builds an index to compare vectors.
4. 🔍 Query is embedded and matched against the index.
5. 🎯 Returns top N most similar products.

---


## 📦 Installation

```bash
git clone https://github.com/BrijeshRakhasiya/Semantic-Search-.git
cd myntra-semantic-search
pip install -r requirements.txt
```

# ▶️ Run the App
```
 streamlit run SearchApp.py
```
#🔧 Technologies Used
- FAISS
- Sentence-Transformers
- Streamlit
- Pandas, NumPy, Scikit-learn

  
## 📄 License

This project is licensed under the MIT License.

---
**Made ❤️ by Brijesh Rakhasiya**
