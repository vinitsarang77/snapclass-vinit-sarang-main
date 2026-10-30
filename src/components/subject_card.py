import streamlit as st

def subject_card(name, code, section, stats=None, footer_callback=None):
    # Updated visual styles for a sleek, modern UI card layout
    html = f"""
        <div style="background-color: #ffffff; 
                    border-left: 6px solid #EB459E; 
                    padding: 24px; 
                    border-radius: 16px; 
                    box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.05), 0 2px 4px -2px rgba(0, 0, 0, 0.05); 
                    border: 1px solid #f1f5f9; 
                    margin-bottom: 16px;
                    font-family: system-ui, -apple-system, sans-serif;">
        <h3 style="margin: 0 0 8px 0; color: #0f172a; font-size: 1.4rem; font-weight: 600;">{name}</h3>
        <p style="color: #64748b; margin: 0 0 16px 0; font-size: 0.95rem;">Code: <span style="background-color: #e0e7ff; color: #4f46e5; padding: 3px 8px; border-radius: 6px; font-weight: 500;">{code}</span> | Section: <span style="color: #334155; font-weight: 500;">{section}</span></p>
        """
    if stats:
        html += """
        <div style="display: flex; gap: 12px; flex-wrap: wrap;">
        """
        for icon, label, value in stats:
            html += f'<div style="background-color: #fdf2f8; color: #be185d; padding: 6px 12px; border-radius: 20px; font-size: 0.85rem; font-weight: 500; display: flex; align-items: center; gap: 4px; border: 1px solid #fce7f3;">{icon} <span><b>{value}</b> {label}</span></div>'

        html += "</div>"
    
    # Close the master card div wrapper securely before injecting layout elements
    html += "</div>"

    st.markdown(html, unsafe_allow_html=True)

    # Fixed: Safely check if the callback function exists before executing it once
    if footer_callback is not None:
        footer_callback()
