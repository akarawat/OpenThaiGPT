import openthaigpt

# OpenThaiGPT Model 0.1.0-beta
'''
print(openthaigpt.generate(instruction="แปลภาษาอังกฤษเป็นภาษาไทย", 
        input="We want to reduce weight.", 
        model_name = "kobkrit/openthaigpt-0.1.0-beta", 
        min_length=50, max_length=300, top_p=0.75, 
        top_k=40, num_beams=1, no_repeat_ngram_size=0, 
        temperature=0.1, early_stopping=True, load_8bit=False))
'''
# เราต้องการลดน้ำหนัก.
# OpenThaiGPT Model 0.1.0-alpha
print(openthaigpt.generate(instruction="ระบุ 5 อาการทั่วไปของ COVID-19", 
        input="", model_name = "kobkrit/openthaigpt-0.1.0-alpha", 
        min_length=50, max_length=1000, top_k=20,
        num_beams=5, no_repeat_ngram_size=10, temperature=1.5,
        early_stopping=True))
'''
print(openthaigpt.generate(instruction="อธิบายขั้นตอนการทำข้าวผัดไก่", 
        input="", model_name = "kobkrit/openthaigpt-0.1.0-alpha", 
        min_length=50, max_length=768, top_k=20,
        num_beams=5, no_repeat_ngram_size=10, temperature=1.5,
        early_stopping=True))
# ขั้นตอนการทำข้าวผัดไก่ ได้แก่ 1. เตรียมไก่และน้ำมันมะพร้าว 2. นำไปผสมกับเนยขาว 3. ใส่เนื้อหมูที่เหลืออยู่ในเครื่องปรุงอาหาร 4. เพิ่มไข่เจียระเบียบ 5. นำผักผัก 6. เต็มไปด้วยแป้งสำหรับผัด 7. ผสานข้อมูลของคุณให้แน่ใจว่าไก่&quot;จะเป็นส่วนประกอบทั้งหมด&quot; 8. นำໄก่ไปใช้ในกระท่อมที

# OpenThaiGPT Model 0.0.4
print(openthaigpt.generate("Q: อยากลดความอ้วนทำไง\n\nA:"))
# Q: อยากลดความอ้วนทำไง
#
# A: การลดน้ำหนักเป็นสิ่งที่สำคัญที่สุดสำหรับการลดไขมันในร่างกาย ดังนั้นคุณควรปรึกษาแพทย์หรือผู้เชี่ยวชาญด้านสุขภาพก่อนที่จะตัดสินใจว่าจะเลือกใช้ผลิตภัณฑ์ใดในการรักษาหรือไม่ อย่างไรก็ตาม หากคุณรู้สึกว่าตัวเองมีปัญหาในเรื่องนี้ คุณสามารถติดต่อแพทย์เพื่อสอบถามข้อมูลเพิ่มเติมเกี่ยวกับวิธีการแก้ไขปัญหานี้ได้เช่นกัน นอกจากนี้คุณยังสามารถพูดคุยกับคนอื่น ๆ เพื่อช่วยให้คำปรึกษาที่ดียิ่งขึ้นได้อีกด้วยค่ะ ขอบคุณที่มา: https://www.facebook.com/pages/%E0%B8%A8-in-the-circle-healthy-make-up.html?mibextid=a&browse=b&country=1&fb=&idx=0&pageb

#####################

# OpenThaiGPT-Zero

# ข้อความจาก OpenThaiGPT
openthaigpt.zero("การลดน้ำหนักเป็นเรื่องที่ต้องพิจารณาอย่างละเอียดและรอบคอบเพื่อให้ได้ผลลัพธ์ที่ดีและมีประสิทธิภาพมากที่สุด")
# {'perplexity': 2.4544131755828857,
# 'threshold': 10,
# 'isGeneratedFromOpenThaiGPT': True}

# ข้อความจาก OpenAI ChatGPT
openthaigpt.zero("สวัสดีครับ มีอะไรให้ผมช่วยเหลือหรือไม่ครับ?")
# {'perplexity': 4.949122428894043,
# 'theshold': 10,
# 'isGeneratedFromOpenThaiGPT': True}

# ข้อความจากมนุษย์
openthaigpt.zero("ทดสอบครับผม")
# {'perplexity': 1758.141357421875,
# 'threshold': 10,
# 'isGeneratedFromOpenThaiGPT': False}

# แสดงวิธีการปรับ threshold
openthaigpt.zero("สวัสดีครับ", threshold=5)
# {'perplexity': 8.109768867492676,
# 'theshold': 5,
# 'isGeneratedFromOpenThaiGPT': False}
'''
