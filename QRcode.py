import qrcode
import streamlit as st

st.image("logo.png",width=250)
st.title("QRcode generator")
st.write("by Caivil Ndobela")

try:
    
    def generate_qr_code(text, file_name):
        #QR Code Configuration
        qrcolor = st.text_input(str("Choose color of qrcode:"))
        bgcolor = st.text_input(str("Choose color of background:"))
        
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=6,
            border=3
        )
        
        qr.add_data(text)
        qr.make(fit=True) #Generating the QR Code, True if Version1 doesnt fit the size
        img=qr.make_image(fill_color=qrcolor,
        back_color=bgcolor)# Creating the Image
        img.save(file_name)
    
    x=st.text_input(str("Input URL:"))
    y=st.text_input(str("Output file_name:"))
    
    if __name__ == "__main__":
        text= x
        file_name= y + ".png"
        
        generate_qr_code(text, file_name)
        
    
    st.image(file_name)
    
    with open(file_name, "rb") as file:
        st.download_button(
            label="Download image",
            data=file,
            file_name=file_name,
            mime="image/png",
        )
    
except ValueError:
    st.error("Please fill in the columns")

st.button("Enter")
    

