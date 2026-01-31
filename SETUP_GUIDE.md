# 🚀 Setup Guide - Bootcamp Generator Web App

## 📁 Struktur Folder yang Dibutuhkan

```
bootcamp-generator/
├── pages/
│   ├── index.tsx                    # Home page (NEW)
│   └── api/
│       └── generate-bootcamp.ts     # API route (SUDAH ADA)
├── components/
│   └── BootcampForm.tsx             # Form component (SUDAH ADA)
├── styles/
│   └── globals.css                  # Global CSS (NEW)
├── scripts/
│   ├── ai_to_json.py               # AI Generator (SUDAH ADA)
│   └── json_to_docx.py             # DOCX Converter (SUDAH ADA)
├── bootcamp.types.ts               # Types (SUDAH ADA)
├── next.config.js                  # Next config (NEW)
├── tailwind.config.js              # Tailwind config (NEW)
├── tsconfig.json                   # TS config (NEW)
├── package.json                    # Dependencies (SUDAH ADA)
├── requirements.txt                # Python deps (SUDAH ADA)
└── .env.local                      # API keys (HARUS DIBUAT)
```

---

## 🎯 Pilihan Setup

### **Option 1: Next.js Full Stack (Recommended untuk Production)** ⭐

#### Step 1: Create Next.js Project
```bash
# Create new Next.js app
npx create-next-app@latest bootcamp-generator
cd bootcamp-generator
```

Pilih options:
- ✅ TypeScript: Yes
- ✅ ESLint: Yes
- ✅ Tailwind CSS: Yes
- ✅ `src/` directory: No
- ✅ App Router: No (use Pages Router)
- ✅ Import alias: Yes (@/*)

#### Step 2: Copy Files ke Project
```bash
# Copy semua downloaded files ke folder project
cp bootcamp.types.ts ./
cp BootcampForm.tsx ./components/
cp api_generate_bootcamp.ts ./pages/api/
cp pages_index.tsx ./pages/index.tsx
cp ai_to_json.py ./scripts/
cp json_to_docx.py ./scripts/
cp requirements.txt ./
```

#### Step 3: Install Dependencies
```bash
# Node.js dependencies
npm install

# Python dependencies
pip install -r requirements.txt
```

#### Step 4: Setup Environment
```bash
# Create .env.local
echo "OPENAI_API_KEY=sk-your-actual-api-key-here" > .env.local
```

#### Step 5: Run Development Server
```bash
npm run dev
```

Buka browser: **http://localhost:3000**

---

### **Option 2: Express.js Simple (Recommended untuk Quick Start)** 🚀

#### Step 1: Create Project Folder
```bash
mkdir bootcamp-generator
cd bootcamp-generator
```

#### Step 2: Copy Files
```bash
# Copy semua downloaded files
cp express_api.js ./
cp ai_to_json.py ./
cp json_to_docx.py ./
cp package.json ./
cp requirements.txt ./
```

#### Step 3: Install Dependencies
```bash
# Node.js
npm install express cors

# Python
pip install openai python-docx
```

#### Step 4: Setup API Key
```bash
echo "OPENAI_API_KEY=sk-your-key" > .env.local
```

#### Step 5: Run Server
```bash
node express_api.js
```

Server running di: **http://localhost:3001**

#### Step 6: Test API dengan Postman atau CURL
```bash
# Test generate bootcamp
curl -X POST http://localhost:3001/api/generate-bootcamp \
  -H "Content-Type: application/json" \
  -d '{
    "nama": "Web Development Bootcamp",
    "durasi": 8,
    "level": "Beginner",
    "deskripsi": "Learn full stack web development"
  }'
```

---

### **Option 3: Standalone HTML (Simple UI)** 📄

Buat file `index.html`:

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Bootcamp Generator</title>
    <script src="https://cdn.tailwindcss.com"></script>
</head>
<body class="bg-gradient-to-br from-blue-50 to-purple-50 min-h-screen p-8">
    <div class="max-w-2xl mx-auto bg-white rounded-lg shadow-lg p-8">
        <h1 class="text-3xl font-bold mb-6">🚀 Bootcamp Generator</h1>
        
        <form id="bootcampForm" class="space-y-4">
            <div>
                <label class="block font-semibold mb-2">Nama Bootcamp</label>
                <input type="text" id="nama" class="w-full border rounded px-4 py-2" required>
            </div>
            
            <div class="grid grid-cols-2 gap-4">
                <div>
                    <label class="block font-semibold mb-2">Durasi (minggu)</label>
                    <input type="number" id="durasi" class="w-full border rounded px-4 py-2" value="8" required>
                </div>
                <div>
                    <label class="block font-semibold mb-2">Level</label>
                    <select id="level" class="w-full border rounded px-4 py-2">
                        <option>Beginner</option>
                        <option>Intermediate</option>
                        <option>Advanced</option>
                    </select>
                </div>
            </div>
            
            <div>
                <label class="block font-semibold mb-2">Deskripsi</label>
                <textarea id="deskripsi" class="w-full border rounded px-4 py-2" rows="4" required></textarea>
            </div>
            
            <button type="submit" class="w-full bg-blue-600 text-white py-3 rounded-lg font-semibold hover:bg-blue-700">
                ✨ Generate dengan AI
            </button>
        </form>
        
        <div id="result" class="mt-8 hidden">
            <h2 class="text-xl font-bold mb-4">✅ Generated Successfully!</h2>
            <pre id="jsonOutput" class="bg-gray-100 p-4 rounded overflow-auto max-h-96 text-sm"></pre>
        </div>
    </div>

    <script>
        document.getElementById('bootcampForm').addEventListener('submit', async (e) => {
            e.preventDefault();
            
            const data = {
                nama: document.getElementById('nama').value,
                durasi: parseInt(document.getElementById('durasi').value),
                level: document.getElementById('level').value,
                deskripsi: document.getElementById('deskripsi').value
            };
            
            try {
                const response = await fetch('http://localhost:3001/api/generate-bootcamp', {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify(data)
                });
                
                const result = await response.json();
                
                document.getElementById('jsonOutput').textContent = JSON.stringify(result, null, 2);
                document.getElementById('result').classList.remove('hidden');
            } catch (error) {
                alert('Error: ' + error.message);
            }
        });
    </script>
</body>
</html>
```

Run dengan:
```bash
# Start Express server dulu
node express_api.js

# Buka index.html di browser (double click atau):
open index.html
```

---

## 🎯 File-File Utama untuk Web

### **Untuk Next.js:**
1. `pages/index.tsx` - Home page dengan form
2. `components/BootcampForm.tsx` - React form component
3. `pages/api/generate-bootcamp.ts` - API endpoint
4. `scripts/ai_to_json.py` - AI generator
5. `scripts/json_to_docx.py` - DOCX converter

### **Untuk Express.js:**
1. `express_api.js` - Backend server (semua endpoint)
2. `ai_to_json.py` - AI generator
3. `json_to_docx.py` - DOCX converter
4. `index.html` - (Optional) Frontend UI

---

## 🧪 Testing

### Test API Health
```bash
curl http://localhost:3001/health
```

### Test Generate
```bash
curl -X POST http://localhost:3001/api/generate-bootcamp \
  -H "Content-Type: application/json" \
  -d '{
    "nama": "React Bootcamp",
    "durasi": 6,
    "level": "Intermediate",
    "deskripsi": "Learn React from scratch"
  }'
```

---

## 🐛 Troubleshooting

### Port Already in Use
```bash
# Kill process on port 3001
lsof -ti:3001 | xargs kill -9

# Or use different port
PORT=4000 node express_api.js
```

### Python Not Found
```bash
# Check Python
which python3

# Use python instead
# Edit express_api.js: change "python3" to "python"
```

### OpenAI API Error
```bash
# Check API key
cat .env.local

# Test API key
python3 -c "from openai import OpenAI; c = OpenAI(); print('OK')"
```

---

## 📦 Quick Command Reference

```bash
# Next.js
npm run dev              # Development
npm run build            # Production build
npm start                # Production server

# Express
node express_api.js      # Start server
npm run api              # Start server (via npm)

# Python standalone
python3 ai_to_json.py --name "Test" --durasi 4 --output test.json
python3 json_to_docx.py --input test.json --output test.docx
```

---

## 🎉 You're Ready!

Pilih salah satu option di atas dan mulai generate bootcamp curriculum! 🚀
