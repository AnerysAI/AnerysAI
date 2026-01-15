"""Code Generation Module untuk AnerysAI"""

class CodeGenerator:
    """Generate kode berdasarkan request user"""
    
    def __init__(self):
        self.templates = {
            "hello_world": self.hello_world,
            "function": self.generate_function,
            "loop": self.generate_loop,
            "list": self.generate_list,
            "dictionary": self.generate_dict,
            "class": self.generate_class,
            "api_get": self.generate_api_get,
            "api_post": self.generate_api_post,
            "html": self.generate_html,
            "calculator": self.generate_calculator,
            "fibonacci": self.generate_fibonacci,
            "factorial": self.generate_factorial,
        }
    
    def hello_world(self):
        return '''print("Hello, World!")
print("Selamat datang!")'''
    
    def generate_function(self, name="greet", param="name"):
        return f'''def {name}({param}):
    """Fungsi untuk menyapa"""
    return f"Halo {{{{param}}}}"

# Penggunaan
result = {name}("AnerysAI")
print(result)'''
    
    def generate_loop(self, count=5):
        return f'''# Loop dari 1 sampai {count}
for i in range(1, {count + 1}):
    print(f"Iterasi: {{i}}")

# Loop dengan list
items = ["Python", "JavaScript", "Java"]
for item in items:
    print(f"Bahasa: {{item}}")'''
    
    def generate_list(self):
        return '''# Create list
fruits = ["apple", "banana", "orange"]
print(f"Buah: {fruits}")

# Add to list
fruits.append("grape")
print(f"Setelah tambah: {fruits}")

# Remove from list
fruits.remove("banana")
print(f"Setelah hapus: {fruits}")

# List operations
print(f"Jumlah: {len(fruits)}")
print(f"Pertama: {fruits[0]}")'''
    
    def generate_dict(self):
        return '''# Create dictionary
person = {
    "nama": "AnerysAI",
    "umur": 3,
    "pekerjaan": "Chatbot",
    "bahasa": "Python"
}

print(f"Nama: {person['nama']}")
print(f"Umur: {person['umur']}")

# Add key-value
person['kota'] = 'Jakarta'
print(person)

# Iterate dictionary
for key, value in person.items():
    print(f"{key}: {value}")'''
    
    def generate_class(self, class_name="Person"):
        return f'''class {class_name}:
    """Kelas {class_name}"""
    
    def __init__(self, nama, umur):
        self.nama = nama
        self.umur = umur
    
    def introduce(self):
        return f"Halo, nama saya {{self.nama}}, umur {{self.umur}}"
    
    def birthday(self):
        self.umur += 1
        return f"Sekarang umur {{self.umur}}"

# Penggunaan
person = {class_name}("AnerysAI", 3)
print(person.introduce())
print(person.birthday())'''
    
    def generate_api_get(self):
        return '''from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/api/hello', methods=['GET'])
def hello():
    """GET endpoint"""
    return jsonify({
        "status": "success",
        "message": "Halo dari API!",
        "data": {
            "name": "AnerysAI",
            "version": "3.0"
        }
    })

@app.route('/api/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    """GET user by ID"""
    return jsonify({
        "id": user_id,
        "name": f"User {user_id}",
        "email": f"user{user_id}@example.com"
    })

if __name__ == '__main__':
    app.run(debug=True, port=5000)'''
    
    def generate_api_post(self):
        return '''from flask import Flask, request, jsonify

app = Flask(__name__)

users_db = []

@app.route('/api/users', methods=['POST'])
def create_user():
    """POST endpoint untuk create user"""
    data = request.json
    
    if not data or 'name' not in data:
        return jsonify({"error": "Name required"}), 400
    
    new_user = {
        "id": len(users_db) + 1,
        "name": data['name'],
        "email": data.get('email', 'unknown@example.com')
    }
    
    users_db.append(new_user)
    
    return jsonify({
        "status": "success",
        "message": "User created",
        "data": new_user
    }), 201

@app.route('/api/users', methods=['GET'])
def get_users():
    """GET semua users"""
    return jsonify({
        "status": "success",
        "data": users_db
    })

if __name__ == '__main__':
    app.run(debug=True, port=5000)'''
    
    def generate_html(self):
        return '''<!DOCTYPE html>
<html lang="id">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>AnerysAI Chatbot</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            max-width: 800px;
            margin: 0 auto;
            padding: 20px;
            background: #f0f0f0;
        }
        .container {
            background: white;
            padding: 20px;
            border-radius: 8px;
            box-shadow: 0 2px 10px rgba(0,0,0,0.1);
        }
        .message {
            margin: 10px 0;
            padding: 10px;
            border-radius: 5px;
        }
        .user-msg {
            background: #e3f2fd;
            text-align: right;
        }
        .bot-msg {
            background: #f1f8e9;
        }
        input {
            width: 100%;
            padding: 10px;
            margin-top: 10px;
            border: 1px solid #ddd;
            border-radius: 4px;
        }
        button {
            padding: 10px 20px;
            background: #2196F3;
            color: white;
            border: none;
            border-radius: 4px;
            cursor: pointer;
            margin-top: 10px;
        }
        button:hover {
            background: #1976D2;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>🤖 AnerysAI Chatbot</h1>
        <div id="chat-box"></div>
        <input type="text" id="user-input" placeholder="Ketik pesan...">
        <button onclick="sendMessage()">Kirim</button>
    </div>
    
    <script>
        function sendMessage() {
            const input = document.getElementById('user-input');
            const message = input.value;
            
            if (!message) return;
            
            // Add user message
            addMessage(message, 'user-msg');
            
            // Simulate bot response
            setTimeout(() => {
                addMessage('Respons dari AnerysAI!', 'bot-msg');
            }, 500);
            
            input.value = '';
        }
        
        function addMessage(text, className) {
            const chatBox = document.getElementById('chat-box');
            const msg = document.createElement('div');
            msg.className = `message ${className}`;
            msg.textContent = text;
            chatBox.appendChild(msg);
            chatBox.scrollTop = chatBox.scrollHeight;
        }
    </script>
</body>
</html>'''
    
    def generate_calculator(self):
        return '''class Calculator:
    """Kalkulator sederhana"""
    
    def add(self, a, b):
        """Tambah"""
        return a + b
    
    def subtract(self, a, b):
        """Kurang"""
        return a - b
    
    def multiply(self, a, b):
        """Kali"""
        return a * b
    
    def divide(self, a, b):
        """Bagi"""
        if b == 0:
            return "Error: Tidak bisa dibagi 0"
        return a / b
    
    def power(self, a, b):
        """Pangkat"""
        return a ** b

# Test
calc = Calculator()
print(f"5 + 3 = {calc.add(5, 3)}")
print(f"10 - 4 = {calc.subtract(10, 4)}")
print(f"7 * 6 = {calc.multiply(7, 6)}")
print(f"20 / 4 = {calc.divide(20, 4)}")
print(f"2 ^ 8 = {calc.power(2, 8)}")'''
    
    def generate_fibonacci(self, n=10):
        return f'''def fibonacci(n):
    """Generate Fibonacci sequence"""
    fib = [0, 1]
    for i in range(2, n):
        fib.append(fib[i-1] + fib[i-2])
    return fib

# Get first {n} Fibonacci numbers
result = fibonacci({n})
print(f"Fibonacci ({n} terms): {{result}}")

# Calculate nth Fibonacci number
def fib_nth(n):
    if n <= 1:
        return n
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b

print(f"Fibonacci(10) = {{fib_nth(10)}}")
print(f"Fibonacci(20) = {{fib_nth(20)}}")'''
    
    def generate_factorial(self, n=5):
        return f'''def factorial(n):
    """Hitung faktorial n"""
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

# Iterative approach
def factorial_iter(n):
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

# Test
print(f"{n}! = {{factorial({n})}}")
print(f"Verif: {n}! = {{factorial_iter({n})}}")

# Calculate multiple
for i in range(1, 6):
    print(f"{{i}}! = {{factorial(i)}}")'''
    
    def generate(self, code_type="hello_world", **kwargs):
        """Generate code berdasarkan tipe"""
        if code_type in self.templates:
            template_func = self.templates[code_type]
            # Call dengan atau tanpa arguments
            try:
                return template_func(**kwargs)
            except TypeError:
                return template_func()
        return f"❌ Tipe kode '{code_type}' tidak tersedia"
    
    def list_templates(self):
        """List semua kode yang bisa di-generate"""
        return list(self.templates.keys())


# Test
if __name__ == "__main__":
    gen = CodeGenerator()
    
    print("=== Hello World ===")
    print(gen.generate("hello_world"))
    print("\n=== Function ===")
    print(gen.generate("function", name="add", param="a, b"))
    print("\n=== Calculator ===")
    print(gen.generate("calculator"))
