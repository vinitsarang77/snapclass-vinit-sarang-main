import streamlit as st

def footer_home():
    logo_url = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSQm4gTZnnLTz59Mr15vcaoDMNCmqnJFBGhFAFMdKaOXg&s=10"
    
    st.markdown(f"""
        <style>
            @keyframes heartbeat {{
                0% {{ transform: scale(1); }}
                50% {{ transform: scale(1.2); }}
                100% {{ transform: scale(1); }}
            }}
            .heart-icon {{
                display: inline-block;
                color: #EB459E;
                animation: heartbeat 1.5s infinite ease-in-out;
                margin: 0 4px;
            }}
            .author-name {{
                background: linear-gradient(135deg, #FFD700 0%, #FF8C00 50%, #EB459E 100%);
                -webkit-background-clip: text;
                -webkit-text-fill-color: transparent;
                font-weight: 800;
                letter-spacing: 0.5px;
            }}
            /* Modern Premium NITIANS Badge with Graduation Icon */
            .nitians-tag {{
                display: inline-flex;
                align-items: center;
                gap: 5px;
                background: linear-gradient(135deg, rgba(255, 255, 255, 0.25) 0%, rgba(255, 255, 255, 0.1) 100%);
                border: 1px solid rgba(255, 255, 255, 0.45);
                padding: 4px 12px;
                border-radius: 20px;
                font-size: 0.8rem;
                font-weight: 800;
                color: #FFFFFF;
                letter-spacing: 0.8px;
                box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
                backdrop-filter: blur(8px);
                -webkit-backdrop-filter: blur(8px);
                transition: all 0.3s cubic-bezier(0.16, 1, 0.3, 1);
                margin-left: 8px;
            }}
            .footer-card {{
                margin-top: 0.5rem;
                display: flex;
                align-items: center;
                justify-content: center;
                gap: 10px;
                padding: 0.75rem 1.75rem;
                background: rgba(255, 255, 255, 0.12);
                backdrop-filter: blur(10px);
                -webkit-backdrop-filter: blur(10px);
                border-radius: 50px;
                border: 1px solid rgba(255, 255, 255, 0.25);
                box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.15);
                width: fit-content;
                margin-left: auto;
                margin-right: auto;
            }}
            .footer-text {{
                font-family: 'Outfit', sans-serif !important;
                font-weight: 500;
                color: #FFFFFF !important;
                font-size: 0.95rem;
                margin: 0 !important;
            }}
            .footer-logo {{
                max-height: 22px;
                border-radius: 4px;
                object-fit: contain;
                transition: transform 0.3s ease;
            }}
            .footer-card:hover .footer-logo {{
                transform: rotate(10deg) scale(1.1);
            }}
        </style>

        <div class="footer-card">
            <p class="footer-text">
                Created with <span class="heart-icon">❤️</span> by 
                <span class="author-name">Vinit Sarang</span>
                <span class="nitians-tag"><span class="grad-icon">🎓</span> NITIAN</span>
            </p>
        </div>
    """, unsafe_allow_html=True)

def footer_dashboard():
    logo_url = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSQm4gTZnnLTz59Mr15vcaoDMNCmqnJFBGhFAFMdKaOXg&s=10"
    
    st.markdown(f"""
        <style>
            @keyframes heartbeat {{
                0% {{ transform: scale(1); }}
                50% {{ transform: scale(1.2); }}
                100% {{ transform: scale(1); }}
            }}
            .heart-icon {{
                display: inline-block;
                color: #EB459E;
                animation: heartbeat 1.5s infinite ease-in-out;
                margin: 0 4px;
            }}
            .author-name {{
                background: linear-gradient(135deg, #FFD700 0%, #FF8C00 50%, #EB459E 100%);
                -webkit-background-clip: text;
                -webkit-text-fill-color: transparent;
                font-weight: 800;
                letter-spacing: 0.5px;
            }}
            /* Modern Premium NITIANS Badge with Graduation Icon */
            .nitians-tag {{
                display: inline-flex;
                align-items: center;
                gap: 5px;
                background: linear-gradient(135deg, rgba(255, 255, 255, 0.25) 0%, rgba(255, 255, 255, 0.1) 100%);
                border: 1px solid rgba(255, 255, 255, 0.45);
                padding: 4px 12px;
                border-radius: 20px;
                font-size: 0.8rem;
                font-weight: 800;
                color: black;
                letter-spacing: 0.8px;
                box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
                backdrop-filter: blur(8px);
                -webkit-backdrop-filter: blur(8px);
                transition: all 0.3s cubic-bezier(0.16, 1, 0.3, 1);
                margin-left: 8px;
            }}
            .footer-card {{
                margin-top: 0.5rem;
                display: flex;
                align-items: center;
                justify-content: center;
                gap: 10px;
                padding: 0.75rem 1.75rem;
                background: rgba(255, 255, 255, 0.12);
                backdrop-filter: blur(10px);
                -webkit-backdrop-filter: blur(10px);
                border-radius: 50px;
                border: 1px solid rgba(255, 255, 255, 0.25);
                box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.15);
                width: fit-content;
                margin-left: auto;
                margin-right: auto;
            }}
            .footer-text {{
                font-family: 'Outfit', sans-serif !important;
                font-weight: 500;
                color: black !important;
                font-size: 0.95rem;
                margin: 0 !important;
            }}
            .footer-logo {{
                max-height: 22px;
                border-radius: 4px;
                object-fit: contain;
                transition: transform 0.3s ease;
            }}
            .footer-card:hover .footer-logo {{
                transform: rotate(10deg) scale(1.1);
            }}
        </style>

        <div class="footer-card">
            <p class="footer-text">
                Created with <span class="heart-icon">❤️</span> by 
                <span class="author-name">Vinit Sarang</span>
                <span class="nitians-tag"><span class="grad-icon">🎓</span> NITIAN</span>
            </p>
        </div>
    """, unsafe_allow_html=True)