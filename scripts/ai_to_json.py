#!/usr/bin/env python3
"""
AI to JSON Generator for Bootcamp Workshop
============================================
Generate Bootcamp Workshop content from AI (OpenAI GPT) and convert to JSON format.
Handles communication with OpenAI API and parsing responses.
"""

import os
import sys
import json
import time
import re
from typing import Optional

# Fix encoding for Windows
if sys.stdout:
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except:
        pass

# Get script and parent directory
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
PARENT_DIR = os.path.dirname(BASE_DIR)

def load_api_key():
    """Load API key from .env.local or environment variable."""
    # Try environment variable first
    api_key = os.environ.get("OPENAI_API_KEY")
    if api_key:
        print("✅ API key loaded from environment variable")
        return api_key
    
    # Try .env.local in parent directory
    env_file = os.path.join(PARENT_DIR, '.env.local')
    if os.path.exists(env_file):
        with open(env_file, 'r', encoding='utf-8') as f:
            for line in f:
                line = line.strip()
                if line.startswith('OPENAI_API_KEY='):
                    api_key = line.split('=', 1)[1].strip()
                    # Remove quotes if present
                    if api_key.startswith('"') and api_key.endswith('"'):
                        api_key = api_key[1:-1]
                    if api_key.startswith("'") and api_key.endswith("'"):
                        api_key = api_key[1:-1]
                    if api_key:
                        print(f"✅ API key loaded from .env.local")
                        return api_key
    
    # Try api_openai.txt in scripts directory
    api_file = os.path.join(BASE_DIR, 'api_openai.txt')
    if os.path.exists(api_file):
        with open(api_file, 'r', encoding='utf-8') as f:
            api_key = f.read().strip()
            if api_key:
                print("✅ API key loaded from api_openai.txt")
                return api_key
    
    # Try api_openai.txt in parent directory
    api_file = os.path.join(PARENT_DIR, 'api_openai.txt')
    if os.path.exists(api_file):
        with open(api_file, 'r', encoding='utf-8') as f:
            api_key = f.read().strip()
            if api_key:
                print("✅ API key loaded from api_openai.txt (parent)")
                return api_key
    
    return None


class BootcampAIGenerator:
    """Generate Bootcamp Workshop JSON content using OpenAI API."""
    
    def __init__(self, api_key: Optional[str] = None):
        """
        Initialize Bootcamp AI Generator.
        
        Args:
            api_key: Optional API key. If not provided, will load from .env.local or api_openai.txt
        """
        self.api_key = api_key or load_api_key()
        self.client = None
        self.model = "gpt-4o-mini"
        
        if self.api_key:
            self._init_client()
        else:
            print("❌ No API key found!")
            print("   Please set OPENAI_API_KEY in one of:")
            print(f"   1. {os.path.join(PARENT_DIR, '.env.local')}")
            print(f"   2. {os.path.join(BASE_DIR, 'api_openai.txt')}")
            print("   3. Environment variable OPENAI_API_KEY")
    
    def _init_client(self) -> bool:
        """Initialize OpenAI client with extended timeout."""
        try:
            from openai import OpenAI
            # Set longer timeout for large generation requests (10 minutes)
            self.client = OpenAI(api_key=self.api_key, timeout=600.0)
            print("✅ OpenAI client initialized with 10-minute timeout")
            return True
        except Exception as e:
            print(f"❌ Error initializing OpenAI client: {e}")
            return False
    
    def generate_prompt(self, bootcamp_name: str, durasi: int = 8, 
                       level: str = "Beginner", tipe: str = "Hybrid",
                       additional_context: str = "") -> str:
        """Generate prompt for OpenAI to create complete Bootcamp content."""

        context_section = ""
        if additional_context.strip():
            context_section = f"\n## Konteks Tambahan:\n{additional_context}\n"

        prompt_template = """Anda adalah ahli dalam merancang program bootcamp dan pelatihan intensif di bidang teknologi. Buatkan Rencana Program Bootcamp/Workshop lengkap untuk:

## Informasi Bootcamp:
- Nama: {bootcamp_name}
- Durasi: {durasi} minggu
- Level: {level}
- Tipe: {tipe}
{context_section}

## Instruksi:
Buatkan bootcamp curriculum dalam format JSON dengan struktur PERSIS seperti berikut. PENTING: Hanya output JSON murni tanpa markdown code block.

{{
  "deskripsi": "Deskripsi lengkap bootcamp 5-7 kalimat yang menjelaskan tujuan, cakupan, metodologi, dan manfaat bootcamp ini",
  "deskripsiSingkat": "Tagline menarik 1 kalimat yang merangkum esensi bootcamp",
  
  "targetPeserta": {{
    "deskripsi": "Deskripsi umum siapa target peserta ideal untuk bootcamp ini",
    "latar_belakang": [
      "Fresh graduate IT/Computer Science",
      "Career switcher yang ingin masuk tech industry",
      "Junior developer yang ingin upgrade skill"
    ],
    "prasyarat_teknis": [
      "Pemahaman dasar programming (minimal 1 bahasa)",
      "Familiar dengan command line/terminal",
      "Memiliki laptop dengan spesifikasi minimum RAM 8GB"
    ],
    "prasyarat_soft_skill": [
      "Komitmen waktu 20-30 jam per minggu",
      "Problem solving mindset",
      "Kemauan belajar mandiri dan kolaboratif"
    ]
  }},
  
  "learningOutcomes": [
    {{
      "kode": "LO-1",
      "pernyataan": "Peserta mampu membangun full-stack web application dari scratch",
      "kategori": "Technical"
    }},
    {{
      "kode": "LO-2",
      "pernyataan": "Peserta mampu bekerja dalam tim menggunakan Git workflow",
      "kategori": "Soft Skill"
    }},
    {{
      "kode": "LO-3",
      "pernyataan": "Peserta memiliki portfolio 3 projects untuk job application",
      "kategori": "Portfolio"
    }}
  ],
  
  "minggu": [
    {{
      "mingguKe": 1,
      "tema": "Introduction & Fundamentals",
      "learningOutcomes": ["LO-1"],
      "materiPokok": [
        "Programming fundamentals review",
        "Development environment setup",
        "Version control with Git"
      ],
      "metodePembelajaran": {{
        "metode": "Lecture + Workshop",
        "deskripsi": "Kombinasi lecture untuk konsep fundamental dengan hands-on workshop untuk memastikan pemahaman praktis dan penguasaan tools development modern",
        "aktivitas": "Mengikuti lecture interaktif memahami konsep dasar mengerjakan coding exercises hands-on setup development environment membuat first commit ke GitHub repository"
      }},
      "waktu": "Lecture 2x120', Workshop 3x180'",
      "pengalamanBelajar": "Peserta akan setup development environment lengkap belajar Git workflow dasar membuat GitHub account dan repository pertama mengerjakan coding challenges fundamental untuk membangun fondasi programming yang kuat",
      "penilaian": {{
        "kriteria": "Kelengkapan setup environment keberhasilan Git operations kualitas coding exercises ketepatan waktu submission aktivitas participation dalam workshop session",
        "bobot": 5
      }}
    }},
    {{
      "mingguKe": 2,
      "tema": "Frontend Development - HTML, CSS, JavaScript",
      "learningOutcomes": ["LO-1"],
      "materiPokok": [
        "HTML5 semantic elements",
        "CSS3 responsive design",
        "JavaScript ES6+ fundamentals"
      ],
      "metodePembelajaran": {{
        "metode": "Workshop + Mini Project",
        "deskripsi": "Workshop intensif frontend development dengan real-world examples diikuti mini project untuk mengaplikasikan semua konsep yang dipelajari dalam project portfolio personal",
        "aktivitas": "Mengikuti live coding workshop membangun responsive web pages mengerjakan JavaScript exercises membuat mini project personal portfolio website dengan HTML CSS JavaScript modern"
      }},
      "waktu": "Workshop 4x180', Project Work 2x120'",
      "project": {{
        "nama": "Personal Portfolio Website",
        "deskripsi": "Membuat responsive portfolio website menggunakan HTML5, CSS3, dan vanilla JavaScript",
        "deliverables": [
          "Responsive portfolio website (mobile & desktop)",
          "GitHub repository dengan clean commit history",
          "Deployed website (Netlify/Vercel)"
        ],
        "teknologi": ["HTML5", "CSS3", "JavaScript ES6+", "Git"]
      }},
      "pengalamanBelajar": "Peserta akan menguasai fundamental frontend development membangun responsive website dari scratch mengimplementasikan modern CSS techniques seperti Flexbox Grid menulis clean JavaScript code deploy website pertama ke production environment",
      "penilaian": {{
        "kriteria": "Kualitas responsive design clean semantic HTML modern CSS implementation functional JavaScript interactivity code quality deployment success presentasi project creativity dan usability website",
        "bobot": 10
      }}
    }}
  ],
  
  "assessment": [
    {{
      "nama": "Participation & Attendance",
      "deskripsi": "Kehadiran aktif dalam session dan partisipasi dalam diskusi",
      "bobot": 10,
      "metode": "Observasi instruktur dan tracking kehadiran",
      "kriteria": [
        "Kehadiran minimum 80% dari total session",
        "Aktif bertanya dan berdiskusi",
        "Membantu sesama peserta"
      ]
    }},
    {{
      "nama": "Weekly Assignments",
      "deskripsi": "Tugas mingguan untuk memperkuat pemahaman",
      "bobot": 25,
      "metode": "Code review dan automated testing",
      "kriteria": [
        "Ketepatan waktu submission",
        "Code quality dan best practices",
        "Functionality dan test coverage"
      ]
    }},
    {{
      "nama": "Mini Projects",
      "deskripsi": "Project kecil untuk mengaplikasikan skill yang dipelajari",
      "bobot": 30,
      "metode": "Project evaluation dan peer review",
      "kriteria": [
        "Implementasi requirement lengkap",
        "Code architecture dan clean code",
        "UI/UX quality",
        "Documentation quality"
      ]
    }},
    {{
      "nama": "Final Capstone Project",
      "deskripsi": "Project akhir comprehensive sebagai portfolio piece",
      "bobot": 35,
      "metode": "Presentation, demo, dan code review",
      "kriteria": [
        "Technical complexity",
        "Innovation dan creativity",
        "Production readiness",
        "Presentation dan demo quality"
      ]
    }}
  ],
  
  "instruktur": [
    {{
      "nama": "John Doe",
      "expertise": ["Full Stack Development", "System Architecture", "DevOps"],
      "peran": "Lead Instructor"
    }},
    {{
      "nama": "Jane Smith",
      "expertise": ["Frontend Development", "UI/UX Design", "React"],
      "peran": "Assistant Instructor"
    }}
  ],
  
  "toolsResources": {{
    "software": [
      "VS Code / IDE pilihan",
      "Git",
      "Node.js & npm",
      "Browser DevTools"
    ],
    "platform": [
      "GitHub/GitLab",
      "Slack untuk komunikasi",
      "Zoom untuk online session",
      "LMS untuk materi"
    ],
    "akun_diperlukan": [
      "GitHub account",
      "Vercel/Netlify account",
      "Discord/Slack workspace"
    ]
  }},
  
  "sertifikasi": {{
    "nama": "Certificate of Completion - {bootcamp_name}",
    "syarat_kelulusan": [
      "Nilai akhir minimal 70%",
      "Kehadiran minimal 80%",
      "Complete final project",
      "Portfolio dengan minimal 3 projects"
    ],
    "nilai_minimal": 70,
    "benefit": [
      "Sertifikat resmi completion",
      "Portfolio projects siap untuk job application",
      "Akses ke alumni network",
      "Career coaching session"
    ]
  }},
  
  "referensi": [
    "MDN Web Docs - https://developer.mozilla.org",
    "freeCodeCamp - https://www.freecodecamp.org",
    "JavaScript.info - Complete JavaScript Tutorial",
    "You Don't Know JS (Book Series) - Kyle Simpson",
    "Eloquent JavaScript - Marijn Haverbeke"
  ]
}}

## Catatan Penting:
- Gunakan bahasa Indonesia yang profesional namun friendly
- Konten harus sangat relevan dengan "{bootcamp_name}"
- Jumlah minggu harus sesuai durasi: {durasi} minggu
- WAJIB untuk setiap minggu:
  * "metodePembelajaran.deskripsi": minimal 20 kata menjelaskan metode dan pendekatan pembelajaran
  * "metodePembelajaran.aktivitas": minimal 20 kata menjelaskan aktivitas konkret peserta
  * "pengalamanBelajar": minimal 30 kata menjelaskan pengalaman dan skill yang didapat
  * "penilaian.kriteria": minimal 20 kata kriteria penilaian yang jelas dan terukur
- Total bobot assessment harus 100%
- Total bobot penilaian mingguan (jika ada) harus 100%
- Learning outcomes harus mencakup: Technical skills, Soft skills, dan Portfolio
- materiPokok harus spesifik dan praktis, bukan generik
- Sesuaikan dengan level: {level} (Beginner = fundamental, Intermediate = applied, Advanced = advanced topics)
- Tipe {tipe}: Online (full remote), Offline (full onsite), Hybrid (kombinasi)
- Variasikan metode pembelajaran: Lecture, Workshop, Project-Based, Case Study, Peer Learning
- Referensi harus nyata dan dapat diakses (buku, website, course online, dokumentasi)

Output JSON saja, tanpa markdown formatting atau penjelasan."""

        return prompt_template.format(
            bootcamp_name=bootcamp_name,
            durasi=durasi,
            level=level,
            tipe=tipe,
            context_section=context_section
        )
    
    def parse_json_response(self, response: str) -> dict:
        """Parse JSON from OpenAI response, handle markdown code blocks and common JSON errors."""
        text = response.strip()
        
        # Handle ```json ... ``` format
        if text.startswith("```"):
            lines = text.split("\n")
            if lines[0].startswith("```"):
                lines = lines[1:]
            if lines and lines[-1].strip() == "```":
                lines = lines[:-1]
            text = "\n".join(lines).strip()
        
        # Try direct parsing first
        try:
            return json.loads(text)
        except json.JSONDecodeError as e:
            print(f"⚠️ First JSON parse attempt failed: {e.msg}")
            print(f"   Attempting to fix common JSON issues...")
            
            original_text = text
            
            # Fix 1: Remove control characters
            try:
                text = ''.join(char if ord(char) >= 32 or char in '\n\r\t' else '' for char in text)
                result = json.loads(text)
                print(f"✅ Fixed JSON by removing control characters")
                return result
            except json.JSONDecodeError:
                pass
            
            # Fix 2: Fix trailing commas
            try:
                text = re.sub(r',(\s*[}\]])', r'\1', original_text)
                result = json.loads(text)
                print(f"✅ Fixed JSON with trailing comma removal")
                return result
            except json.JSONDecodeError:
                pass
            
            # Fix 3: Extract JSON object manually
            try:
                start_idx = original_text.find('{')
                if start_idx == -1:
                    raise ValueError("No JSON object found")
                
                bracket_count = 0
                in_string = False
                escape_next = False
                
                for i in range(start_idx, len(original_text)):
                    char = original_text[i]
                    
                    if escape_next:
                        escape_next = False
                        continue
                    
                    if char == '\\':
                        escape_next = True
                        continue
                    
                    if char == '"':
                        in_string = not in_string
                        continue
                    
                    if not in_string:
                        if char == '{':
                            bracket_count += 1
                        elif char == '}':
                            bracket_count -= 1
                            if bracket_count == 0:
                                json_str = original_text[start_idx:i+1]
                                result = json.loads(json_str)
                                print(f"✅ Fixed JSON by extracting valid JSON substring")
                                return result
                
                raise ValueError("Could not find matching closing bracket")
                
            except Exception as e3:
                print(f"❌ Could not extract valid JSON: {e3}")
                print(f"   Response preview (first 500 chars):")
                print(f"   {original_text[:500]}")
                raise json.JSONDecodeError(
                    f"Failed to parse JSON after multiple fix attempts",
                    original_text[:100],
                    0
                )
    
    def send_message(self, prompt: str, max_retries: int = 3) -> Optional[str]:
        """
        Send message to OpenAI and get response.
        
        Args:
            prompt: The prompt to send
            max_retries: Maximum number of retries on failure
            
        Returns:
            Response text or None if failed
        """
        if not self.client:
            print("❌ OpenAI client not initialized")
            return None
        
        for attempt in range(max_retries):
            try:
                print(f"🤖 Sending message to OpenAI (attempt {attempt + 1}/{max_retries})...")
                print(f"   Model: {self.model}")
                
                response = self.client.chat.completions.create(
                    model=self.model,
                    messages=[
                        {"role": "system", "content": "You are an expert in designing intensive bootcamp and workshop programs in technology and coding."},
                        {"role": "user", "content": prompt}
                    ],
                    temperature=0.7
                )
                
                if response.choices and len(response.choices) > 0:
                    content = response.choices[0].message.content
                    if content:
                        print(f"✅ Received response from OpenAI ({len(content)} chars)")
                        return content
                
                print("⚠️ Empty response from OpenAI")
                return None
                
            except Exception as e:
                error_str = str(e)
                print(f"❌ Error on attempt {attempt + 1}: {error_str}")
                
                if attempt < max_retries - 1:
                    wait_time = (2 ** attempt) * 3
                    print(f"⏳ Waiting {wait_time} seconds before retry...")
                    time.sleep(wait_time)
                else:
                    print("❌ All retry attempts failed")
                    import traceback
                    traceback.print_exc()
                    return None
        
        return None
    
    def generate_bootcamp_json(self, bootcamp_name: str, durasi: int = 8,
                               level: str = "Beginner", tipe: str = "Hybrid",
                               additional_context: str = "") -> Optional[dict]:
        """
        Generate complete Bootcamp content as JSON.
        
        Args:
            bootcamp_name: Name of the bootcamp
            durasi: Duration in weeks
            level: Beginner/Intermediate/Advanced
            tipe: Online/Offline/Hybrid
            additional_context: Additional context for AI generation
            
        Returns:
            Dictionary with Bootcamp data or None if failed
        """
        print(f"\n📝 Generating Bootcamp Curriculum for: {bootcamp_name}")
        print("=" * 60)
        
        if not self.client:
            print("❌ Cannot generate - OpenAI client not initialized")
            return None
        
        prompt = self.generate_prompt(bootcamp_name, durasi, level, tipe, additional_context)
        response = self.send_message(prompt)
        
        if not response:
            print("❌ Failed to get response from OpenAI")
            return None
        
        try:
            bootcamp_data = self.parse_json_response(response)
            print("✅ Bootcamp JSON generated successfully!")
            print(f"   - Learning Outcomes: {len(bootcamp_data.get('learningOutcomes', []))} items")
            print(f"   - Weekly Schedule: {len(bootcamp_data.get('minggu', []))} weeks")
            print(f"   - Assessment Components: {len(bootcamp_data.get('assessment', []))} items")
            print(f"   - Instructors: {len(bootcamp_data.get('instruktur', []))} people")
            print(f"   - References: {len(bootcamp_data.get('referensi', []))} items")
            return bootcamp_data
        except json.JSONDecodeError as e:
            print(f"❌ Failed to parse JSON: {e}")
            print(f"Response preview: {response[:500]}...")
            return None


# Standalone usage
if __name__ == "__main__":
    import argparse
    
    parser = argparse.ArgumentParser(description="Generate Bootcamp Curriculum JSON using OpenAI")
    parser.add_argument("--name", default="Full Stack Web Development Bootcamp", help="Bootcamp name")
    parser.add_argument("--durasi", type=int, default=8, help="Duration in weeks")
    parser.add_argument("--level", default="Beginner", choices=["Beginner", "Intermediate", "Advanced"], help="Bootcamp level")
    parser.add_argument("--tipe", default="Hybrid", choices=["Online", "Offline", "Hybrid"], help="Bootcamp type")
    parser.add_argument("--context", default="", help="Additional context for generation")
    parser.add_argument("--output", default="bootcamp_generated.json", help="Output JSON file")
    
    args = parser.parse_args()
    
    print("🚀 Bootcamp AI Generator")
    print("=" * 60)
    
    generator = BootcampAIGenerator()
    
    if not generator.client:
        print("\n❌ Failed to initialize - check API key")
        sys.exit(1)
    
    bootcamp_data = generator.generate_bootcamp_json(
        bootcamp_name=args.name,
        durasi=args.durasi,
        level=args.level,
        tipe=args.tipe,
        additional_context=args.context
    )
    
    if bootcamp_data:
        with open(args.output, 'w', encoding='utf-8') as f:
            json.dump(bootcamp_data, f, ensure_ascii=False, indent=2)
        print(f"\n✅ JSON saved to: {args.output}")
    else:
        print("\n❌ Failed to generate Bootcamp JSON")
        sys.exit(1)
