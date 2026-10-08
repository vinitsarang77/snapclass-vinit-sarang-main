import streamlit as st

def style_background_home():

    st.markdown("""
            <style>
                .stApp{
                    background: #5865f2 !important
                }

                /* Card container styling using stColumn data-testid */
            div[data-testid="stColumn"] {
                background: rgba(224, 227, 255, 0.92) !important;
                backdrop-filter: blur(12px) !important;
                -webkit-backdrop-filter: blur(12px) !important;
                padding: 2.5rem 2rem !important;
                border-radius: 2rem !important;
                border: 1px solid rgba(255, 255, 255, 0.4) !important;
                box-shadow: 0 15px 35px rgba(0, 0, 0, 0.15) !important;
                transition: transform 0.3s ease, box-shadow 0.3s ease !important;
                text-align: center !important;
            }

                .stApp div[data-testid="stColumn"]:hover {
                    transform: translateY(-6px) !important;
                    box-shadow: 0 20px 40px rgba(0, 0, 0, 0.22) !important;
                    }

            /* Center images and elements inside cards */
            div[data-testid="stColumn"] img {
                display: block !important;
                margin: 0.1rem auto !important;
                border-radius: 15% !important;
                box-shadow: 0 8px 20px rgba(88, 101, 242, 0.25) !important;
                transition: transform 0.3s ease !important;
            }

            div[data-testid="stColumn"]:hover img {
                transform: scale(1.06) !important;
            }

            
            </style>
                """, unsafe_allow_html=True)

def style_background_dashboard():

    st.markdown("""
            <style>
                .stApp{
                    background: #E0E3FF !important
                }
            </style>
                """, unsafe_allow_html=True)

def style_base_layout():

    st.markdown("""
                <style>
                @import url('https://fonts.googleapis.com/css2?family=Climate+Crisis:YEAR@1979&display=swap');
                @import url('https://fonts.googleapis.com/css2?family=Outfit:wght@100..900&display=swap');
                    /* Hide Top Bar of Streamlit */
    
                    #MainMenu, footer, header {
                        visibility: hidden;
                        }

                    .block-container {
                        padding-top:1.5rem !important;
                    }

                    h1 { 
                        font-family: 'Climate Crisis', sans-serif !important;
                        font-size: 3.5rem !important;
                        line-height:1.1 !important;
                        margin-bottom:0rem !important;
                        
                    }

                    h2 { 
                        font-family: 'Climate Crisis', sans-serif !important;
                        font-size: 2rem !important;
                        line-height:0.9 !important;
                        margin-bottom:0rem !important;
                        }

                    h3, h4, p{
                        font-family: 'Outfit', sans-serif !important;
                    }

                    /* Base Button Styling */
            button[data-testid="baseButton-secondary"], 
            button[data-testid="baseButton-primary"] {
                border-radius: 1.25rem !important;
                font-family: 'Outfit', sans-serif !important;
                font-weight: 600 !important;
                font-size: 1rem !important;
                padding: 0.65rem 1.8rem !important;
                background: #5865F2 !important;
                color: #FFFFFF !important;
                border: none !important;
                box-shadow: 0 6px 18px rgba(88, 101, 242, 0.35) !important;
                transition: all 0.25s cubic-bezier(0.4, 0, 0.2, 1) !important;
                cursor: pointer !important;
            }

                    button {
                        border-radius: 1.5rem !important;
                        color: white !important;
                        padding: 10px 20px !important;
                        background: #5865F2 !important;
                        border: none !important;
                        transition: transform 0.25s ease-in-out !important;
                    }

                    /* Secondary & Tertiary Variants */
            button[kind="secondary"] {
                background: #EB459E !important;
                box-shadow: 0 6px 18px rgba(235, 69, 158, 0.35) !important;
            }

            button[kind="tertiary"] {
                background: #111827 !important;
                box-shadow: 0 6px 18px rgba(17, 24, 39, 0.25) !important;
            }

            /* Button Hover & Active States */
            button:hover {
                transform: translateY(-2px) scale(1.02) !important;
                box-shadow: 0 10px 22px rgba(0, 0, 0, 0.25) !important;
            }
            button:active {
                transform: translateY(0px) scale(0.98) !important;
            }
                </style>
                    """, unsafe_allow_html=True)