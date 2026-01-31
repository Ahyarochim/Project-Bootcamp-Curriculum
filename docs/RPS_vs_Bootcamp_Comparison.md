# 📊 Perbandingan: RPS vs Bootcamp Generator

## Overview

| Aspek | RPS Generator | Bootcamp Generator |
|-------|---------------|-------------------|
| **Target** | Mata kuliah perguruan tinggi | Bootcamp/workshop intensif |
| **Durasi** | 16 minggu (1 semester) | 1-24 minggu (flexible) |
| **Format** | Akademis formal | Professional training |
| **Evaluasi** | UTS, UAS, tugas | Projects, portfolio, demo |

## 🎯 Struktur Data

### RPS (Mata Kuliah)
```typescript
{
  identitas: {
    kode: "MK001",
    nama: "Praktikum Mekatronika",
    sks: 2,
    semester: 4,
    status: "Wajib",
    prasyarat: "Elektronika Dasar"
  },
  cpl: [...],           // Capaian Pembelajaran Lulusan
  ik: [...],            // Indikator Kinerja
  cpmk: [...],          // Capaian Pembelajaran MK
  minggu: [16 weeks],   // Fixed 16 minggu
  penilaian: {
    N1: 20%, N2: 30%, N3: 10%, 
    N4: 20% (UTS), N5: 20% (UAS)
  }
}
```

### Bootcamp (Workshop)
```typescript
{
  identitas: {
    nama: "Full Stack Bootcamp",
    kode: "BOOT-001",
    durasi: 8,  // Flexible
    level: "Beginner",
    tipe: "Hybrid",
    kapasitas: 25
  },
  learningOutcomes: [...],  // Technical + Soft + Portfolio
  targetPeserta: {...},      // Background, prerequisites
  minggu: [flexible weeks],  // 1-24 minggu
  assessment: [             // Flexible components
    { nama: "Participation", bobot: 10% },
    { nama: "Assignments", bobot: 25% },
    { nama: "Projects", bobot: 30% },
    { nama: "Capstone", bobot: 35% }
  ]
}
```

## 📋 Komponen Unik

### RPS Only
- ✅ CPL (Capaian Pembelajaran Lulusan)
- ✅ CPMK (Capaian Pembelajaran Mata Kuliah)
- ✅ IK (Indikator Kinerja)
- ✅ Mapping CPL → CPMK → IK
- ✅ Fixed UTS (minggu 8) & UAS (minggu 16)
- ✅ N1-N5 assessment framework
- ✅ Otoritas (Koordinator, Dekan, dll)

### Bootcamp Only
- ✅ Target Peserta (latar belakang, prasyarat)
- ✅ Learning Outcomes (Technical, Soft Skill, Portfolio)
- ✅ Project-based learning dengan deliverables
- ✅ Instructor profiles dengan expertise
- ✅ Tools & Resources (software, platform, hardware)
- ✅ Sertifikasi dengan benefits
- ✅ Fasilitas dan Investasi info
- ✅ Flexible duration (1-24 minggu)

## 🔄 Weekly Schedule Comparison

### RPS Minggu
```typescript
{
  mingguKe: 1,
  kemampuanAkhir: "CPMK 3-2",
  bahanKajian: "Pengenalan Mekatronika",
  metodePembelajaran: {
    metode: "TM SCL" | "CBL" | "PBL" | "PjBL",
    deskripsi: "20 kata",
    aktivitas: "20 kata"
  },
  waktu: "3x50'",
  pengalamanBelajar: "30 kata",
  penilaian: {
    kriteria: "20 kata",
    bobotMateri: 5  // Total 100% dari 14 minggu
  }
}
```

### Bootcamp Minggu
```typescript
{
  mingguKe: 1,
  tema: "Web Development Fundamentals",
  learningOutcomes: ["LO-1", "LO-2"],
  materiPokok: ["HTML5", "CSS3", "JavaScript"],
  metodePembelajaran: {
    metode: "Lecture + Workshop",
    deskripsi: "20+ kata",
    aktivitas: "20+ kata"
  },
  waktu: "Lecture 2x120', Workshop 4x180'",
  project?: {  // Optional
    nama: "Portfolio Website",
    deliverables: [...],
    teknologi: [...]
  },
  pengalamanBelajar: "30+ kata",
  penilaian?: {  // Optional per minggu
    kriteria: "20+ kata",
    bobot: 10
  }
}
```

## 🎓 Assessment Models

### RPS Assessment
```
Fixed Components:
- N1 (Partisipatif): 20%
- N2 (Project/Case Based): 30%
- N3 (Kuis): 10%
- N4 (UTS): 20%
- N5 (UAS): 20%
Total: 100%

Mapped ke CPMK dengan bobot spesifik
```

### Bootcamp Assessment
```
Flexible Components:
- Participation & Attendance: 10%
- Weekly Assignments: 20-30%
- Mini Projects: 20-30%
- Final Capstone: 30-40%
Total: 100%

Focus on portfolio dan practical skills
```

## 🔧 Metode Pembelajaran

### RPS Methods
- **TM SCL** (Student Centered Learning) - Teori
- **CBL** (Case Based Learning) - Studi kasus
- **PBL** (Problem Based Learning) - Problem solving
- **PjBL** (Project Based Learning) - Praktikum

Format waktu: `3x50'` atau `2x170'`

### Bootcamp Methods
- **Lecture** - Conceptual teaching
- **Workshop** - Hands-on practice
- **Project-Based** - Real-world projects
- **Case Study** - Industry scenarios
- **Peer Learning** - Collaboration
- **Mentoring** - One-on-one guidance

Format waktu: `Lecture 2x120', Workshop 3x180'`

## 🤖 AI Generation Differences

### RPS AI Prompt Focus
- Academic language (Bahasa Indonesia formal)
- CPL-CPMK-IK mapping consistency
- Fixed 16 minggu structure
- UTS/UAS placement (minggu 8/16)
- N1-N5 bobot calculation
- Referensi akademis (jurnal, buku)

### Bootcamp AI Prompt Focus
- Professional yet friendly language
- Practical skill outcomes
- Flexible duration (1-24 minggu)
- Industry-relevant projects
- Tools & technology stack
- Mixed references (books, docs, online courses)

## 💼 Use Cases

### RPS Generator
✅ Mata kuliah universitas  
✅ Program studi perguruan tinggi  
✅ Akreditasi akademik  
✅ Kurikulum formal  
✅ Semester-based learning  

### Bootcamp Generator
✅ Coding bootcamps  
✅ Professional workshops  
✅ Corporate training  
✅ Skill upgrade programs  
✅ Career switcher programs  
✅ Intensive learning programs  

## 📄 Document Output

### RPS DOCX
- Cover dengan institusi
- Otoritas signatures
- CPL-CPMK-IK tables
- 16 minggu detail
- Penilaian breakdown
- Referensi akademis

### Bootcamp DOCX
- Professional cover page
- Target peserta section
- Learning outcomes
- Flexible weekly schedule
- Project highlights
- Instructor bios
- Tools & resources list
- Certification info
- Investment/pricing (optional)

## 🎯 Rekomendasi Penggunaan

### Gunakan RPS Generator jika:
- Membuat kurikulum mata kuliah formal
- Butuh format akreditasi perguruan tinggi
- Fixed 16 minggu semester
- Perlu CPL-CPMK mapping
- Target: mahasiswa S1/D4

### Gunakan Bootcamp Generator jika:
- Membuat program pelatihan intensif
- Flexible duration (1-24 minggu)
- Focus pada portfolio projects
- Target: professionals, career switchers
- Butuh info instruktur & pricing

## 🔄 Kemungkinan Hybrid

Bisa combine kedua approach:
```typescript
{
  // RPS-style academic rigor
  cpl: [...],
  cpmk: [...],
  
  // Bootcamp-style flexibility
  targetPeserta: {...},
  projects: [...],
  instructors: [...],
  
  // Flexible components
  durasi: 12,  // Bisa non-16
  assessment: "custom"
}
```

## 📊 Feature Matrix

| Feature | RPS | Bootcamp |
|---------|-----|----------|
| AI Generation | ✅ | ✅ |
| React Form | ✅ | ✅ |
| JSON to DOCX | ✅ | ✅ |
| TypeScript Types | ✅ | ✅ |
| Python Backend | ✅ | ✅ |
| Fixed Duration | ✅ (16) | ❌ (1-24) |
| CPL Mapping | ✅ | ❌ |
| Project Focus | ⚠️ | ✅ |
| Instructor Profiles | ❌ | ✅ |
| Tools & Resources | ⚠️ | ✅ |
| Certificate Info | ❌ | ✅ |
| Pricing Info | ❌ | ✅ (optional) |

## 🎓 Conclusion

**RPS Generator** = Academic, formal, structured untuk perguruan tinggi  
**Bootcamp Generator** = Practical, flexible, project-focused untuk professional training

Kedua sistem bisa digunakan bersamaan dalam satu platform dengan UI yang memilih template mana yang akan digunakan!

---

*Both systems complement each other untuk different educational contexts* 🎯
