# İçe Aktarma
from flask import Flask, render_template, request

app = Flask(__name__)

def result_calculate(size, lights, device):
    # Elektrikli cihazların enerji tüketimini hesaplamaya olanak tanıyan değişkenler
    home_coef = 100
    light_coef = 0.04
    devices_coef = 5   
    return size * home_coef + lights * light_coef + device * devices_coef 

def save_to_file(name, email, address, date):
    with open("form.txt", "a", encoding="utf-8") as f:
        f.write(f"İsim: {name}\nE-posta: {email}\nAdres: {address}\nTarih: {date}\n---\n")

# İlk sayfa
@app.route('/')
def index():
    return render_template('index.html')

# İkinci sayfa
@app.route('/<size>')
def lights(size):
    return render_template(
                            'lights.html', 
                            size=size
                           )

# Üçüncü sayfa
@app.route('/<size>/<lights>')
def electronics(size, lights):
    return render_template(
                            'electronics.html',                           
                            size = size, 
                            lights = lights                           
                           )

# Hesaplama
@app.route('/<size>/<lights>/<device>')
def end(size, lights, device):
    return render_template('end.html', 
                            result=result_calculate(int(size),
                                                    int(lights), 
                                                    int(device)
                                                    )
                        )
# Form
@app.route('/form')
def form():
    return render_template('form.html')

#Formun sonuçları
@app.route('/submit', methods=['POST'])
def submit_form():
    # Veri toplama için değişkenleri tanımlayın
    _name = request.form['name']
    _email= request.form['email']
    _address= request.form['address']
    _date= request.form['date']

    save_to_file(_name, _email, _address, _date)

    # Verilerinizi kaydedebilir veya e-posta ile gönderebilirsiniz
    return render_template('form_result.html', 
                           # Değişkenleri buraya yerleştirin
                           name=_name,
                           email=_email,
                           address=_address,
                           date=_date
                           )
if __name__ == '__main__':
    app.run(debug=True)
