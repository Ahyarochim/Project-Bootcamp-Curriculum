/**
 * Bootcamp Workshop Data Types
 * Struktur untuk Rencana Program Workshop / Bootcamp
 */

// ============ IDENTITAS BOOTCAMP ============
export interface IdentitasBootcamp {
  nama: string;                    // Nama Bootcamp (e.g., "Full Stack Web Development Bootcamp")
  kode: string;                    // Kode Bootcamp (e.g., "BOOT-001")
  durasi: number;                  // Durasi dalam minggu
  tipe: string;                    // Tipe: "Online" | "Offline" | "Hybrid"
  level: string;                   // Level: "Beginner" | "Intermediate" | "Advanced"
  kapasitas: number;               // Jumlah peserta maksimal
}

// ============ TARGET PESERTA ============
export interface TargetPeserta {
  deskripsi: string;               // Deskripsi umum target peserta
  latar_belakang: string[];        // Array latar belakang yang cocok
  prasyarat_teknis: string[];      // Prasyarat teknis yang diperlukan
  prasyarat_soft_skill: string[];  // Soft skills yang diharapkan
}

// ============ LEARNING OUTCOMES ============
export interface LearningOutcome {
  kode: string;                    // e.g., "LO-1"
  pernyataan: string;              // Deskripsi learning outcome
  kategori: string;                // "Technical" | "Soft Skill" | "Portfolio"
}

// ============ METODE PEMBELAJARAN ============
export interface MetodePembelajaran {
  metode: string;                  // Jenis metode (Lecture, Workshop, Project, etc.)
  deskripsi: string;               // Penjelasan metode (min 20 kata)
  aktivitas: string;               // Aktivitas peserta (min 20 kata)
}

// ============ PROJECT/CASE STUDY ============
export interface ProjectBootcamp {
  nama: string;                    // Nama project
  deskripsi: string;               // Deskripsi project
  deliverables: string[];          // Hasil yang harus diserahkan
  teknologi: string[];             // Teknologi yang digunakan
}

// ============ WEEKLY SCHEDULE ============
export interface MingguBootcamp {
  mingguKe: number;                // Minggu ke-
  tema: string;                    // Tema minggu ini
  learningOutcomes: string[];      // Array kode LO yang dicapai (e.g., ["LO-1", "LO-2"])
  materiPokok: string[];           // Array materi pokok yang diajarkan
  metodePembelajaran: MetodePembelajaran;
  waktu: string;                   // e.g., "Lecture 2x120', Workshop 3x180'"
  project?: ProjectBootcamp;       // Optional project untuk minggu ini
  pengalamanBelajar: string;       // Pengalaman belajar (min 30 kata)
  penilaian?: {
    kriteria: string;              // Kriteria penilaian (min 20 kata)
    bobot: number;                 // Bobot penilaian (%)
  };
}

// ============ ASSESSMENT/PENILAIAN ============
export interface KomponenPenilaian {
  nama: string;                    // Nama komponen (e.g., "Participation", "Mini Project")
  deskripsi: string;               // Deskripsi komponen
  bobot: number;                   // Bobot dalam persen (%)
  metode: string;                  // Metode penilaian
  kriteria: string[];              // Kriteria penilaian
}

// ============ INSTRUKTUR ============
export interface Instruktur {
  nama: string;
  expertise: string[];             // Area keahlian
  peran: string;                   // e.g., "Lead Instructor", "Assistant", "Mentor"
  kontak?: string;                 // Optional kontak
}

// ============ TOOLS & RESOURCES ============
export interface ToolsResources {
  software: string[];              // Software yang digunakan
  platform: string[];              // Platform pembelajaran
  hardware?: string[];             // Hardware requirement (optional)
  akun_diperlukan: string[];       // Akun yang perlu dibuat peserta
}

// ============ SERTIFIKAT ============
export interface SertifikasiBootcamp {
  nama: string;                    // Nama sertifikat
  syarat_kelulusan: string[];      // Syarat untuk lulus
  nilai_minimal: number;           // Nilai minimal untuk lulus (%)
  benefit: string[];               // Benefit yang didapat
}

// ============ REFERENSI ============
export type ReferensiBootcamp = string;

// ============ COMPLETE BOOTCAMP DATA ============
export interface BootcampData {
  // Metadata
  id?: string;
  createdAt?: string;
  updatedAt?: string;

  // Content
  identitas: IdentitasBootcamp;
  deskripsi: string;               // Deskripsi lengkap bootcamp
  deskripsiSingkat: string;        // Tagline/deskripsi singkat
  targetPeserta: TargetPeserta;
  learningOutcomes: LearningOutcome[];
  minggu: MingguBootcamp[];        // Array weekly schedule
  assessment: KomponenPenilaian[]; // Komponen penilaian
  instruktur: Instruktur[];        // Tim instruktur
  toolsResources: ToolsResources;
  sertifikasi: SertifikasiBootcamp;
  referensi: ReferensiBootcamp[];
  fasilitas?: string[];            // Optional fasilitas yang disediakan
  investasi?: {                    // Optional info biaya
    biaya: number;
    early_bird?: number;
    cicilan?: boolean;
    beasiswa?: boolean;
  };
}

// ============ DEFAULT / EMPTY BOOTCAMP ============
export const createEmptyBootcamp = (): BootcampData => ({
  identitas: {
    nama: '',
    kode: '',
    durasi: 8,
    tipe: 'Hybrid',
    level: 'Beginner',
    kapasitas: 20,
  },
  deskripsi: '',
  deskripsiSingkat: '',
  targetPeserta: {
    deskripsi: '',
    latar_belakang: [],
    prasyarat_teknis: [],
    prasyarat_soft_skill: [],
  },
  learningOutcomes: [],
  minggu: Array.from({ length: 8 }, (_, i) => ({
    mingguKe: i + 1,
    tema: '',
    learningOutcomes: [],
    materiPokok: [],
    metodePembelajaran: {
      metode: '',
      deskripsi: '',
      aktivitas: '',
    },
    waktu: 'Lecture 2x120\', Workshop 3x180\'',
    pengalamanBelajar: '',
  })),
  assessment: [],
  instruktur: [],
  toolsResources: {
    software: [],
    platform: [],
    akun_diperlukan: [],
  },
  sertifikasi: {
    nama: '',
    syarat_kelulusan: [],
    nilai_minimal: 70,
    benefit: [],
  },
  referensi: [],
});

// ============ HELPER TYPES ============
export interface BootcampFormInput {
  nama: string;
  durasi: number;
  level: string;
  deskripsi: string;
  additional_context?: string;
}

export interface BootcampGenerationResult {
  success: boolean;
  data?: BootcampData;
  error?: string;
}
