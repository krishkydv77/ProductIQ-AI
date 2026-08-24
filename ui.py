import requests
import streamlit as st


st.set_page_config(
    page_title="ProductIQ AI",
    page_icon="🧠",
    layout="centered"
)


API_URL = "http://127.0.0.1:8000"


st.markdown(
    """
    <style>
    .block-container {
        max-width: 850px;
        padding-top: 3rem;
    }

    h1 {
        text-align: center;
        font-size: 38px !important;
    }

    h2 {
        text-align: center;
    }

    </style>
    """,
    unsafe_allow_html=True
)



st.caption("PRODUCT INTELLIGENCE PLATFORM")

st.title("ProductIQ AI")

st.subheader("Intelligent Product Research & Discovery")

st.write(
    "AI-powered product intelligence platform for "
    "searching, analyzing, ranking, and discovering "
    "relevant products from your catalog."
)


st.divider()



st.subheader("Find your product")

st.caption(
    "Search products from your catalog."
)


query = st.text_input(
    "Product Search",
    placeholder="e.g. black sports shoes under ₹2500"
)


if st.button(
    "🔎 Search Products",
    type="primary",
    use_container_width=True
):

    if not query.strip():

        st.warning(
            "Please enter a product search."
        )

    else:

        try:

            with st.spinner(
                "Searching products..."
            ):

                response = requests.get(
                    f"{API_URL}/search",
                    params={
                        "q": query
                    },
                    timeout=15
                )


            response.raise_for_status()

            data = response.json()


            # ------------------------------------------------
            # HANDLE API RESPONSE
            # ------------------------------------------------

            if isinstance(data, list):

                products = data

            elif isinstance(data, dict):

                products = (
                    data.get("results")
                    or data.get("products")
                    or data.get("data")
                    or []
                )

            else:

                products = []


            # ------------------------------------------------
            # RESULTS
            # ------------------------------------------------

            if not products:

                st.info(
                    "No products found."
                )

            else:

                st.divider()

                st.subheader(
                    "Search Results"
                )

                st.caption(
                    f'Results for "{query}"'
                )


                # ------------------------------------------------
                # PRODUCT RESULTS
                # ------------------------------------------------

                for product in products:

                    if not isinstance(
                        product,
                        dict
                    ):
                        continue


                    name = (
                        product.get("name")
                        or product.get("product_name")
                        or "Unnamed Product"
                    )


                    category = (
                        product.get("category")
                        or "Product"
                    )


                    price = (
                        product.get("price")
                        or 0
                    )


                    score = (
                        product.get("match_score")
                        or product.get("score")
                        or 0
                    )


                    st.write(
                        f"### 🛍️ {name}"
                    )


                    st.write(
                        f"Category: {category}"
                    )


                    if price:

                        st.write(
                            f"**Price: ₹{price}**"
                        )


                    if score:

                        st.write(
                            f"**Match: {float(score):.1f}%**"
                        )


                    st.divider()


        except requests.exceptions.ConnectionError:

            st.error(
                f"FastAPI server is not running at {API_URL}"
            )


        except requests.exceptions.Timeout:

            st.error(
                "API request timed out."
            )


        except requests.exceptions.HTTPError as error:

            st.error(
                f"API Error: {error}"
            )


        except Exception as error:

            st.error(
                f"Something went wrong: {error}"
            )




st.caption(
    "ProductIQ AI · FastAPI · spaCy · TF-IDF · MySQL"
)