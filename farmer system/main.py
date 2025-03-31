from flask import Flask,render_template,request,session,redirect,url_for,flash
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import login_user,logout_user,login_manager,LoginManager
from flask_login import login_required,current_user


# MY db connection
local_server= True
app = Flask(__name__)
app.secret_key='harshithbhaskar'


# this is for getting unique user access
login_manager=LoginManager(app)
login_manager.login_view='login'

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://Panchadip:9064379751%40Panchadip@localhost/farmer'
db=SQLAlchemy(app)

# here we will create db models that is tables
class Test(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(100))

class Farming(db.Model):
    fid=db.Column(db.Integer,primary_key=True)
    farmingtype=db.Column(db.String(100))


class Addagroproducts(db.Model):
    username=db.Column(db.String(50))
    email=db.Column(db.String(50))
    pid=db.Column(db.Integer,primary_key=True)
    productname=db.Column(db.String(100))
    productdesc=db.Column(db.String(300))
    price=db.Column(db.Integer)



class Trig(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    fid=db.Column(db.String(100))
    action=db.Column(db.String(100))
    timestamp=db.Column(db.String(100))


class User(UserMixin,db.Model):
    id=db.Column(db.Integer,primary_key=True)
    username=db.Column(db.String(50))
    email=db.Column(db.String(50),unique=True)
    password=db.Column(db.String(1000))

class Register(db.Model):
    rid=db.Column(db.Integer,primary_key=True)
    farmername=db.Column(db.String(50))
    adharnumber=db.Column(db.String(50))
    age=db.Column(db.Integer)
    gender=db.Column(db.String(50))
    phonenumber=db.Column(db.String(50))
    address=db.Column(db.String(50))
    farming=db.Column(db.String(50))

    

@app.route('/')
def index(): 
    return render_template('index.html')

@app.route('/farmerdetails')
@login_required
def farmerdetails():
    # query=db.engine.execute(f"SELECT * FROM `register`") 
    query=Register.query.all()
    return render_template('farmerdetails.html',query=query)

@app.route('/agroproducts')
def agroproducts():
    # query=db.engine.execute(f"SELECT * FROM `addagroproducts`") 
    query=Addagroproducts.query.all()
    return render_template('agroproducts.html',query=query)

@app.route('/addagroproduct',methods=['POST','GET'])
@login_required
def addagroproduct():
    if request.method=="POST":
        username=request.form.get('username')
        email=request.form.get('email')
        productname=request.form.get('productname')
        productdesc=request.form.get('productdesc')
        price=request.form.get('price')
        products=Addagroproducts(username=username,email=email,productname=productname,productdesc=productdesc,price=price)
        db.session.add(products)
        db.session.commit()
        flash("Product Added","info")
        return redirect('/agroproducts')
   
    return render_template('addagroproducts.html')

@app.route('/triggers')
@login_required
def triggers():
    # query=db.engine.execute(f"SELECT * FROM `trig`") 
    query=Trig.query.all()
    return render_template('triggers.html',query=query)

@app.route('/addfarming',methods=['POST','GET'])
@login_required
def addfarming():
    if request.method=="POST":
        farmingtype=request.form.get('farming')
        query=Farming.query.filter_by(farmingtype=farmingtype).first()
        if query:
            flash("Farming Type Already Exist","warning")
            return redirect('/addfarming')
        dep=Farming(farmingtype=farmingtype)
        db.session.add(dep)
        db.session.commit()
        flash("Farming Addes","success")
    return render_template('farming.html')




@app.route("/delete/<string:rid>",methods=['POST','GET'])
@login_required
def delete(rid):
    # db.engine.execute(f"DELETE FROM `register` WHERE `register`.`rid`={rid}")
    post=Register.query.filter_by(rid=rid).first()
    db.session.delete(post)
    db.session.commit()
    flash("Slot Deleted Successful","warning")
    return redirect('/farmerdetails')


@app.route("/edit/<string:rid>", methods=['POST', 'GET'])
@login_required
def edit(rid):
    if request.method == "POST":
        farmername = request.form.get('farmername')
        adharnumber = request.form.get('adharnumber')
        age = request.form.get('age')
        gender = request.form.get('gender')
        phonenumber = request.form.get('phonenumber')
        address = request.form.get('address')
        farmingtype = request.form.get('farmingtype')

        # Validate required fields
        if not farmername or not adharnumber or not age:
            flash("Farmer Name, Aadhar Number, and Age are required fields.", "danger")
            return redirect(f'/edit/{rid}')

        # Update the record
        post = Register.query.filter_by(rid=rid).first()
        post.farmername = farmername
        post.adharnumber = adharnumber
        post.age = age
        post.gender = gender
        post.phonenumber = phonenumber
        post.address = address
        post.farming = farmingtype
        db.session.commit()
        flash("Record updated successfully!", "success")
        return redirect('/farmerdetails')

    posts = Register.query.filter_by(rid=rid).first()
    farming = Farming.query.all()
    return render_template('edit.html', posts=posts, farming=farming)


@app.route('/signup',methods=['POST','GET'])
def signup():
    if request.method == "POST":
        username=request.form.get('username')
        email=request.form.get('email')
        password=request.form.get('password')
        print(username,email,password)
        user=User.query.filter_by(email=email).first()
        if user:
            flash("Email Already Exist","warning")
            return render_template('/signup.html')
        # encpassword=generate_password_hash(password)

        # new_user=db.engine.execute(f"INSERT INTO `user` (`username`,`email`,`password`) VALUES ('{username}','{email}','{encpassword}')")

        # this is method 2 to save data in db
        newuser=User(username=username,email=email,password=password)
        db.session.add(newuser)
        db.session.commit()
        flash("Signup Succes Please Login","success")
        return render_template('login.html')

          

    return render_template('signup.html')

@app.route('/login',methods=['POST','GET'])
def login():
    if request.method == "POST":
        email=request.form.get('email')
        password=request.form.get('password')
        user=User.query.filter_by(email=email).first()

        if user and user.password == password:
            login_user(user)
            flash("Login Success","primary")
            return redirect(url_for('index'))
        else:
            flash("invalid credentials","warning")
            return render_template('login.html')    

    return render_template('login.html')

@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash("Logout SuccessFul","warning")
    return redirect(url_for('login'))


from sqlalchemy import text  # Import the `text` function for raw SQL queries

@app.route('/sql_queries')
def sql_queries():
    try:
        # Use a connection to execute raw SQL queries
        with db.engine.connect() as connection:
            max_price = connection.execute(text("SELECT MAX(price) AS max_price FROM addagroproducts")).fetchone()
            min_price = connection.execute(text("SELECT MIN(price) AS min_price FROM addagroproducts")).fetchone()
            avg_price = connection.execute(text("SELECT AVG(price) AS avg_price FROM addagroproducts")).fetchone()
            sum_price = connection.execute(text("SELECT SUM(price) AS sum_price FROM addagroproducts")).fetchone()
            count_products = connection.execute(text("SELECT COUNT(*) AS total_products FROM addagroproducts")).fetchone()
            most_expensive = connection.execute(text("SELECT productname, price FROM addagroproducts ORDER BY price DESC LIMIT 1")).fetchone()
            cheapest = connection.execute(text("SELECT productname, price FROM addagroproducts ORDER BY price ASC LIMIT 1")).fetchone()
            avg_age = connection.execute(text("SELECT AVG(age) AS avg_age FROM register")).fetchone()
            total_farmers = connection.execute(text("SELECT COUNT(*) AS total_farmers FROM register")).fetchone()

        # Pass results to the front end
        return render_template(
            'sql_queries.html',
            max_price=max_price[0],
            min_price=min_price[0],
            avg_price=avg_price[0],
            sum_price=sum_price[0],
            count_products=count_products[0],
            most_expensive=most_expensive,
            cheapest=cheapest,
            avg_age=avg_age[0],
            total_farmers=total_farmers[0]
        )
    except Exception as e:
        return f"An error occurred: {e}"

@app.route('/register',methods=['POST','GET'])
@login_required
def register():
    farming=Farming.query.all()
    if request.method=="POST":
        farmername=request.form.get('farmername')
        adharnumber=request.form.get('adharnumber')
        age=request.form.get('age')
        gender=request.form.get('gender')
        phonenumber=request.form.get('phonenumber')
        address=request.form.get('address')
        farmingtype=request.form.get('farmingtype')     
        query=Register(farmername=farmername,adharnumber=adharnumber,age=age,gender=gender,phonenumber=phonenumber,address=address,farming=farmingtype)
        db.session.add(query)
        db.session.commit()
        # query=db.engine.execute(f"INSERT INTO `register` (`farmername`,`adharnumber`,`age`,`gender`,`phonenumber`,`address`,`farming`) VALUES ('{farmername}','{adharnumber}','{age}','{gender}','{phonenumber}','{address}','{farmingtype}')")
        # flash("Your Record Has Been Saved","success")
        return redirect('/farmerdetails')
    return render_template('farmer.html',farming=farming)



@app.route('/test')
def test():
    try:
        Test.query.all()
        return 'My database is Connected'
    except:
        return 'My db is not Connected'

@app.route('/clear_triggers', methods=['POST'])
def clear_triggers():
    try:
        # Clear all records from the triggers table
        db.engine.execute("DELETE FROM triggers")
        flash("All trigger records have been cleared successfully!", "success")
    except Exception as e:
        flash(f"An error occurred: {e}", "danger")
    return redirect('/triggers')

@app.route('/custom_sql_queries', methods=['GET', 'POST'])
@login_required
def custom_sql_queries():
    farmers = []
    selected_query = None  # To store the selected query type
    if request.method == 'POST':
        query_type = request.form.get('query_type')
        selected_query = query_type  # Store the selected query type
        with db.engine.connect() as connection:  # Use a connection object
            if query_type == 'low_income':
                result = connection.execute(text("SELECT * FROM register WHERE age < 30"))
                farmers = result.fetchall()
            elif query_type == 'high_income':
                result = connection.execute(text("SELECT * FROM register WHERE age > 50"))
                farmers = result.fetchall()
            elif query_type == 'specific_farming':
                result = connection.execute(text("SELECT * FROM register WHERE farming = 'Seed Farming'"))
                farmers = result.fetchall()
            elif query_type == 'age_between_25_40':
                result = connection.execute(text("SELECT * FROM register WHERE age BETWEEN 25 AND 40"))
                farmers = result.fetchall()
            elif query_type == 'gender_distribution':
                result = connection.execute(text("SELECT gender, COUNT(*) AS total FROM register GROUP BY gender"))
                farmers = result.fetchall()
            
            elif query_type == 'top_5_oldest':
                result = connection.execute(text("SELECT * FROM register ORDER BY age DESC LIMIT 5"))
                farmers = result.fetchall()
            elif query_type == 'longest_address':
                result = connection.execute(text("SELECT * FROM register ORDER BY LENGTH(address) DESC LIMIT 1"))
                farmers = result.fetchall()
            elif query_type == 'duplicate_adhar':
                result = connection.execute(text("SELECT adharnumber, COUNT(*) AS count FROM register GROUP BY adharnumber HAVING count > 1"))
                farmers = result.fetchall()
            elif query_type == 'total_farmers':
                result = connection.execute(text("SELECT COUNT(*) AS total_farmers FROM register"))
                farmers = result.fetchall()
            elif query_type == 'average_age':
                result = connection.execute(text("SELECT AVG(age) AS average_age FROM register"))
                farmers = result.fetchall()

    return render_template('custom_sql_queries.html', farmers=farmers, selected_query=selected_query)

app.run(debug=True)
