# 🚀 Bootcamp Workshop Curriculum Generator

Sistem lengkap untuk membuat **Rencana Program Bootcamp/Workshop** dengan AI Generator, form input React, dan export ke DOCX.

## 📋 Fitur Utama

### ✨ Core Features
- **AI Generator** - Auto-generate complete bootcamp curriculum menggunakan OpenAI GPT
- **React Form** - Modern input interface dengan validation
- **JSON Data Structure** - Structured data yang mudah di-manage
- **DOCX Export** - Convert JSON ke professional Word document
- **Backend API** - RESTful API untuk integrasi frontend-backend
- **TypeScript Support** - Fully typed untuk development experience yang lebih baik

### 📦 Komponen Bootcamp
- **Identitas Bootcamp** - Nama, kode, durasi, level, tipe, kapasitas
- **Target Peserta** - Latar belakang, prasyarat teknis & soft skills
- **Learning Outcomes** - Technical, Soft Skills, Portfolio outcomes
- **Weekly Schedule** - Jadwal mingguan dengan materi, metode, project
- **Assessment** - Komponen penilaian dengan bobot dan kriteria
- **Instruktur** - Tim pengajar dengan expertise
- **Tools & Resources** - Software, platform, hardware requirements
- **Sertifikasi** - Syarat kelulusan dan benefits
- **Referensi** - Buku, dokumentasi, online resources

## 🏗️ Struktur Project

```
TASK 1/
├── bootcamp-generator/        # Next.js Application
│   ├── app/
│   │   ├── components/
│   │   │   └── BootcampForm.tsx   # React form component
│   │   ├── types/
│   │   │   └── bootcamp.types.ts  # TypeScript definitions
│   │   ├── page.tsx               # Main page
│   │   ├── layout.tsx
│   │   └── globals.css
│   ├── package.json
│   └── ...
├── scripts/                   # Python Scripts
│   ├── ai_to_json.py          # AI Generator
│   └── json_to_docx.py        # JSON to DOCX converter
├── docs/                      # Documentation
│   ├── PROJECT_SUMMARY.md
│   └── RPS_vs_Bootcamp_Comparison.md
├── templates/                 # JSON Templates
│   └── bootcamp_schema.json   # Example JSON structure
├── express_api.js             # Express.js API server
├── index.html                 # Standalone HTML form
├── bootcamp.types.ts          # TypeScript types (backup)
├── BootcampForm.tsx           # React form (backup)
├── package.json               # Node.js dependencies
├── requirements.txt           # Python dependencies
├── README.md                  # This file
└── SETUP_GUIDE.md             # Setup instructions
```

## 🔧 Setup & Installation

### Prerequisites
- **Node.js** 18+ dan npm/yarn
- **Python** 3.8+
- **OpenAI API Key**

### 1️⃣ Install Dependencies

#### Node.js Dependencies
```bash
npm install
# atau
yarn install
```

#### Python Dependencies
```bash
pip install -r requirements.txt
# atau
pip install openai python-docx
```

### 2️⃣ Setup OpenAI API Key

Buat file `.env.local` di root directory:
```env
OPENAI_API_KEY=sk-your-api-key-here
```

Atau buat file `api_openai.txt`:
```
sk-your-api-key-here
```

## 🎯 Usage

### Option 1: Standalone Python Script

#### Generate Bootcamp JSON dengan AI
```bash
python3 scripts/ai_to_json.py \
  --name "Full Stack Web Development Bootcamp" \
  --durasi 8 \
  --level "Beginner" \
  --context "Fokus pada MERN Stack, include DevOps basics" \
  --output "bootcamp_generated.json"
```

#### Convert JSON ke DOCX
```bash
python3 scripts/json_to_docx.py \
  --input "bootcamp_generated.json" \
  --output "bootcamp_curriculum.docx"
```

### Option 2: Express API Server

#### Start Server
```bash
node express_api.js
```

Server akan berjalan di `http://localhost:3001`

#### API Endpoints

**Generate Bootcamp**
```bash
curl -X POST http://localhost:3001/api/generate-bootcamp \
  -H "Content-Type: application/json" \
  -d '{
    "nama": "Full Stack Web Development Bootcamp",
    "durasi": 8,
    "level": "Beginner",
    "deskripsi": "Intensive bootcamp untuk jadi full-stack developer",
    "additional_context": "Fokus MERN Stack, include DevOps"
  }'
```

**Convert to DOCX**
```bash
curl -X POST http://localhost:3001/api/convert-to-docx \
  -H "Content-Type: application/json" \
  -d @bootcamp_generated.json \
  --output bootcamp_curriculum.docx
```

### Option 3: Next.js Integration

Copy `api_generate_bootcamp.ts` ke `pages/api/` directory dan import `BootcampForm.tsx` component:

```tsx
import { BootcampFormContainer } from '@/components/BootcampForm';

export default function Home() {
  return <BootcampFormContainer />;
}
```

## 📝 JSON Data Structure

### Minimal Example
```json
{
  "identitas": {
    "nama": "Full Stack Bootcamp",
    "kode": "BOOT-001",
    "durasi": 8,
    "tipe": "Hybrid",
    "level": "Beginner",
    "kapasitas": 25
  },
  "deskripsi": "Bootcamp description...",
  "deskripsiSingkat": "Tagline...",
  "targetPeserta": {
    "deskripsi": "Target audience description",
    "latar_belakang": ["Background 1", "Background 2"],
    "prasyarat_teknis": ["Tech prerequisite 1"],
    "prasyarat_soft_skill": ["Soft skill 1"]
  },
  "learningOutcomes": [
    {
      "kode": "LO-1",
      "pernyataan": "Learning outcome statement",
      "kategori": "Technical"
    }
  ],
  "minggu": [
    {
      "mingguKe": 1,
      "tema": "Week theme",
      "learningOutcomes": ["LO-1"],
      "materiPokok": ["Topic 1", "Topic 2"],
      "metodePembelajaran": {
        "metode": "Lecture + Workshop",
        "deskripsi": "Method description...",
        "aktivitas": "Student activities..."
      },
      "waktu": "Lecture 2x120', Workshop 3x180'",
      "pengalamanBelajar": "Learning experience...",
      "penilaian": {
        "kriteria": "Assessment criteria...",
        "bobot": 10
      }
    }
  ],
  "assessment": [...],
  "instruktur": [...],
  "toolsResources": {...},
  "sertifikasi": {...},
  "referensi": [...]
}
```

Lihat `bootcamp_schema.json` untuk complete example.

## 🎨 React Form Component

### Basic Usage
```tsx
import { BootcampForm } from '@/components/BootcampForm';

function MyPage() {
  const handleSubmit = (formData) => {
    console.log('Form submitted:', formData);
    // Navigate to detailed editor or save data
  };

  const handleGenerateAI = async (formData) => {
    const response = await fetch('/api/generate-bootcamp', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(formData)
    });
    const data = await response.json();
    console.log('AI Generated:', data);
  };

  return (
    <BootcampForm
      onSubmit={handleSubmit}
      onGenerateAI={handleGenerateAI}
    />
  );
}
```

## 🔌 API Integration

### Generate Bootcamp
**Endpoint:** `POST /api/generate-bootcamp`

**Request:**
```json
{
  "nama": "Full Stack Web Development Bootcamp",
  "durasi": 8,
  "level": "Beginner",
  "deskripsi": "Intensive bootcamp to become job-ready developer",
  "additional_context": "Focus on MERN stack, include DevOps basics"
}
```

**Response:**
```json
{
  "success": true,
  "data": {
    "id": "boot-1706599200000",
    "identitas": {...},
    "deskripsi": "...",
    "learningOutcomes": [...],
    "minggu": [...],
    ...
  }
}
```

### Convert to DOCX
**Endpoint:** `POST /api/convert-to-docx`

**Request:** Send complete bootcamp JSON data

**Response:** DOCX file download

## 🎯 AI Generator Features

### Auto-Generated Content
- ✅ Complete weekly schedule (8-24 minggu)
- ✅ Learning outcomes (Technical + Soft Skills + Portfolio)
- ✅ Detailed materi pokok per minggu
- ✅ Metode pembelajaran (Lecture, Workshop, Project-Based, dll)
- ✅ Project assignments dengan deliverables
- ✅ Assessment rubrics dan criteria
- ✅ Instructor profiles
- ✅ Tools & resources recommendations
- ✅ References (books, docs, courses)

### Customization Options
- **Durasi**: 1-24 minggu (default: 8)
- **Level**: Beginner, Intermediate, Advanced
- **Tipe**: Online, Offline, Hybrid
- **Additional Context**: Custom requirements untuk AI

## 📄 DOCX Output

Generated DOCX document includes:
- 📑 Professional cover page
- 📝 Complete bootcamp description
- 👥 Target peserta breakdown
- 🎯 Learning outcomes dengan kategorisasi
- 📅 Weekly schedule (detailed)
- 📊 Assessment components dengan bobot
- 👨‍🏫 Instructor profiles
- 🛠️ Tools & resources list
- 🏆 Certification requirements
- 📚 References

## 🔒 Environment Variables

Create `.env.local`:
```env
# OpenAI API
OPENAI_API_KEY=sk-your-api-key-here

# Optional: API Configuration
API_TIMEOUT=300000
MAX_DURATION=300
```

## 🐛 Troubleshooting

### Python Script Errors
```bash
# Check Python version
python3 --version  # Should be 3.8+

# Install dependencies
pip install -r requirements.txt --upgrade

# Test OpenAI connection
python3 -c "from openai import OpenAI; print('OK')"
```

### API Key Issues
```bash
# Verify API key is loaded
python3 -c "import os; print(os.path.exists('.env.local'))"

# Test API key
python3 scripts/ai_to_json.py --name "Test" --durasi 1 --output test.json
```

### DOCX Generation Issues
```bash
# Install python-docx
pip install python-docx --upgrade

# Test conversion
python3 scripts/json_to_docx.py --input templates/bootcamp_schema.json --output test.docx
```

## 📦 Dependencies

### Node.js
- `next` - Next.js framework (if using Next.js)
- `react` - React library
- `typescript` - TypeScript
- `express` - Express.js (if using Express)
- `cors` - CORS middleware

### Python
- `openai` - OpenAI API client
- `python-docx` - DOCX file generation

## 🚀 Deployment

### Vercel (Next.js)
```bash
vercel deploy
```

### Railway/Render (Express)
```bash
# Add Procfile
echo "web: node express_api.js" > Procfile

# Deploy
railway up
# atau
render deploy
```

## 🤝 Contributing

Contributions welcome! Areas for improvement:
- [ ] Add more learning outcome templates
- [ ] Support multiple languages
- [ ] PDF export option
- [ ] Database integration
- [ ] User authentication
- [ ] Bootcamp analytics

## 📜 License

MIT License - feel free to use for your projects!

## 🙋 Support

Butuh bantuan? Create an issue atau contact developer.

---

**Made with ❤️ by Mahasiswa Teknologi Rekayasa Otomasi**

*Transform your bootcamp ideas into professional curriculum documents in minutes!* 🎓
