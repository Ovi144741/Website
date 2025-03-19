import streamlit as st
import datetime

# ---- PAGE CONFIGURATION ----
st.set_page_config(page_title="My Modern Blog", page_icon="📝", layout="wide")

# ---- CUSTOM CSS STYLING ----
st.markdown("""
    <style>
        /* Background Styling */
        body {
            background-color: #f8f9fa;
        }

        /* Blog Title */
        .main-title {
            text-align: center;
            font-size: 3rem;
            font-weight: bold;
            color: #222;
            margin-bottom: 10px;
        }

        /* Blog Subtitle */
        .subtitle {
            text-align: center;
            font-size: 1.3rem;
            color: #666;
            margin-bottom: 30px;
        }

        /* Blog Post Title */
        .post-title {
            font-size: 2rem;
            font-weight: bold;
            color: #007BFF;
            margin-bottom: 5px;
        }

        /* Post Date */
        .post-date {
            font-size: 0.9rem;
            color: #888;
            margin-bottom: 15px;
        }

        /* Post Content */
        .post-content {
            font-size: 1.1rem;
            color: #444;
        }

        /* Navigation Sidebar */
        .css-1d391kg {
            background-color: #222 !important;
            color: white !important;
        }

        /* Success Message */
        .stAlert {
            background-color: #d4edda !important;
            color: #155724 !important;
            border-left: 5px solid #28a745 !important;
        }

        /* Publish Button */
        .stButton>button {
            background-color: #007BFF;
            color: white;
            font-size: 1rem;
            border-radius: 8px;
            padding: 10px 20px;
        }

        /* Footer */
        .footer {
            text-align: center;
            font-size: 0.9rem;
            color: #777;
            margin-top: 50px;
        }
    </style>
""", unsafe_allow_html=True)

# ---- SIDEBAR NAVIGATION ----
st.sidebar.title("📌 Navigation")
menu = st.sidebar.radio("Go to", ["🏠 Home", "📝 Write a Post", "👤 About"])

# ---- SESSION STATE FOR BLOG POSTS ----
if "posts" not in st.session_state:
    st.session_state.posts = []

# ---- HOME PAGE ----
if menu == "🏠 Home":
    st.markdown('<h1 class="main-title">📖 My Modern Blog</h1>', unsafe_allow_html=True)
    st.markdown('<p class="subtitle">A place to share thoughts and ideas</p>', unsafe_allow_html=True)

    if not st.session_state.posts:
        st.info("No blog posts yet. Click on 'Write a Post' to add one!")
    else:
        for post in reversed(st.session_state.posts):
            with st.container():
                st.markdown(f'<h2 class="post-title">{post["title"]}</h2>', unsafe_allow_html=True)
                st.markdown(f'<p class="post-date">📝 {post["date"]}</p>', unsafe_allow_html=True)
                st.markdown(f'<p class="post-content">{post["content"]}</p>', unsafe_allow_html=True)
                st.markdown("---")

# ---- NEW POST PAGE ----
elif menu == "📝 Write a Post":
    st.markdown('<h1 class="main-title">📝 Create a New Blog Post</h1>', unsafe_allow_html=True)

    with st.form("blog_form"):
        title = st.text_input("Post Title", placeholder="Enter a catchy title...")
        content = st.text_area("Post Content", placeholder="Write something amazing...", height=200)
        submitted = st.form_submit_button("🚀 Publish Post")

        if submitted and title and content:
            st.session_state.posts.append({
                "title": title,
                "content": content,
                "date": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            })
            st.success("🎉 Your blog post has been published!")

# ---- ABOUT PAGE ----
elif menu == "👤 About":
    st.markdown('<h1 class="main-title">👤 About Me</h1>', unsafe_allow_html=True)

    col1, col2 = st.columns([1, 2])

    with col1:
        st.image("https://via.placeholder.com/200", width=200)

    with col2:
        st.write("Hi! I'm a passionate blogger who loves sharing insights and experiences. 🌎")
        st.write("This blog is built using [Streamlit](https://streamlit.io/). Hope you enjoy reading!")

# ---- FOOTER ----
st.markdown('<p class="footer">Made with ❤️ using Streamlit</p>', unsafe_allow_html=True)
