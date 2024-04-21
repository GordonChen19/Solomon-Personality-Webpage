from flask import Blueprint, render_template,request,url_for,redirect

views = Blueprint('views', __name__)

@views.route('/', methods=['GET', 'POST'])
def home():
    if(request.method=='POST'):
        pescio={'P':[1,3,11,26,28,33],'E':[4,15,18,20,25,30],'S':[6,10,17,23,29,35],
            'C':[2,8,14,22,31,34],'I':[5,9,13,19,24,27],'O':[0,7,12,16,21,32]}
        P,E,S,C,I,O=0,0,0,0,0,0
        for key, value in pescio.items():
            for question in value:
                if(key=='P'):
                    P+=int(request.form.get('q'+str(question)))
                elif(key=='E'):
                    E+=int(request.form.get('q'+str(question)))
                elif(key=='S'):
                    S+=int(request.form.get('q'+str(question)))
                elif(key=='C'):
                    C+=int(request.form.get('q'+str(question)))
                elif(key=='I'):
                    I+=int(request.form.get('q'+str(question)))
                else:
                    O+=int(request.form.get('q'+str(question)))
        
        P*=3.33
        E*=3.33
        S*=3.33
        C*=3.33
        I*=3.33
        O*=3.33
        
        return redirect(url_for('views.result',P=P,E=E,S=S,C=C,I=I,O=O))
    return render_template("index.html")

@views.route('/results', methods=['GET', 'POST'])
def result():
    P = request.args.get('P')
    E = request.args.get('E')
    S = request.args.get('S')
    C = request.args.get('C')
    I = request.args.get('I')
    O = request.args.get('O')
    return render_template("results.html",P=P,E=E,S=S,C=C,I=I,O=O)