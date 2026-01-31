import React, { useState } from 'react';
import { BootcampData, BootcampFormInput, createEmptyBootcamp } from './bootcamp.types';

interface BootcampFormProps {
  onSubmit: (data: BootcampFormInput) => void;
  onGenerateAI?: (data: BootcampFormInput) => void;
  loading?: boolean;
}

export const BootcampForm: React.FC<BootcampFormProps> = ({ 
  onSubmit, 
  onGenerateAI,
  loading = false 
}) => {
  const [formData, setFormData] = useState<BootcampFormInput>({
    nama: '',
    durasi: 8,
    level: 'Beginner',
    deskripsi: '',
    additional_context: ''
  });

  const [errors, setErrors] = useState<Partial<Record<keyof BootcampFormInput, string>>>({});

  const handleChange = (e: React.ChangeEvent<HTMLInputElement | HTMLTextAreaElement | HTMLSelectElement>) => {
    const { name, value } = e.target;
    setFormData(prev => ({
      ...prev,
      [name]: name === 'durasi' ? parseInt(value) || 0 : value
    }));
    
    // Clear error when user starts typing
    if (errors[name as keyof BootcampFormInput]) {
      setErrors(prev => ({ ...prev, [name]: undefined }));
    }
  };

  const validate = (): boolean => {
    const newErrors: Partial<Record<keyof BootcampFormInput, string>> = {};

    if (!formData.nama.trim()) {
      newErrors.nama = 'Nama bootcamp wajib diisi';
    }

    if (formData.durasi < 1 || formData.durasi > 24) {
      newErrors.durasi = 'Durasi harus antara 1-24 minggu';
    }

    if (!formData.deskripsi.trim()) {
      newErrors.deskripsi = 'Deskripsi bootcamp wajib diisi';
    }

    setErrors(newErrors);
    return Object.keys(newErrors).length === 0;
  };

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault();
    if (validate()) {
      onSubmit(formData);
    }
  };

  const handleGenerateAI = () => {
    if (validate() && onGenerateAI) {
      onGenerateAI(formData);
    }
  };

  return (
    <div className="max-w-4xl mx-auto p-6 bg-white rounded-lg shadow-lg">
      <div className="mb-8">
        <h1 className="text-3xl font-bold text-gray-900 mb-2">
          🚀 Bootcamp Curriculum Generator
        </h1>
        <p className="text-gray-600">
          Buat rencana program bootcamp/workshop dengan AI atau isi manual
        </p>
      </div>

      <form onSubmit={handleSubmit} className="space-y-6">
        {/* Nama Bootcamp */}
        <div>
          <label htmlFor="nama" className="block text-sm font-semibold text-gray-700 mb-2">
            Nama Bootcamp *
          </label>
          <input
            type="text"
            id="nama"
            name="nama"
            value={formData.nama}
            onChange={handleChange}
            placeholder="e.g., Full Stack Web Development Bootcamp"
            className={`w-full px-4 py-3 border rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent ${
              errors.nama ? 'border-red-500' : 'border-gray-300'
            }`}
            disabled={loading}
          />
          {errors.nama && (
            <p className="mt-1 text-sm text-red-600">{errors.nama}</p>
          )}
        </div>

        {/* Durasi & Level */}
        <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
          <div>
            <label htmlFor="durasi" className="block text-sm font-semibold text-gray-700 mb-2">
              Durasi (minggu) *
            </label>
            <input
              type="number"
              id="durasi"
              name="durasi"
              value={formData.durasi}
              onChange={handleChange}
              min="1"
              max="24"
              className={`w-full px-4 py-3 border rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent ${
                errors.durasi ? 'border-red-500' : 'border-gray-300'
              }`}
              disabled={loading}
            />
            {errors.durasi && (
              <p className="mt-1 text-sm text-red-600">{errors.durasi}</p>
            )}
          </div>

          <div>
            <label htmlFor="level" className="block text-sm font-semibold text-gray-700 mb-2">
              Level Bootcamp *
            </label>
            <select
              id="level"
              name="level"
              value={formData.level}
              onChange={handleChange}
              className="w-full px-4 py-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent"
              disabled={loading}
            >
              <option value="Beginner">Beginner</option>
              <option value="Intermediate">Intermediate</option>
              <option value="Advanced">Advanced</option>
            </select>
          </div>
        </div>

        {/* Deskripsi */}
        <div>
          <label htmlFor="deskripsi" className="block text-sm font-semibold text-gray-700 mb-2">
            Deskripsi Bootcamp *
          </label>
          <textarea
            id="deskripsi"
            name="deskripsi"
            value={formData.deskripsi}
            onChange={handleChange}
            rows={4}
            placeholder="Jelaskan tujuan, target peserta, dan outcome dari bootcamp ini..."
            className={`w-full px-4 py-3 border rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent ${
              errors.deskripsi ? 'border-red-500' : 'border-gray-300'
            }`}
            disabled={loading}
          />
          {errors.deskripsi && (
            <p className="mt-1 text-sm text-red-600">{errors.deskripsi}</p>
          )}
        </div>

        {/* Additional Context (Optional for AI) */}
        <div>
          <label htmlFor="additional_context" className="block text-sm font-semibold text-gray-700 mb-2">
            Konteks Tambahan (Opsional - untuk AI Generator)
          </label>
          <textarea
            id="additional_context"
            name="additional_context"
            value={formData.additional_context}
            onChange={handleChange}
            rows={3}
            placeholder="Berikan informasi tambahan seperti teknologi spesifik yang ingin diajarkan, target industri, atau kebutuhan khusus lainnya..."
            className="w-full px-4 py-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent"
            disabled={loading}
          />
          <p className="mt-1 text-xs text-gray-500">
            Informasi ini akan membantu AI menggenerate konten yang lebih spesifik dan relevan
          </p>
        </div>

        {/* Action Buttons */}
        <div className="flex flex-col sm:flex-row gap-4 pt-4">
          {onGenerateAI && (
            <button
              type="button"
              onClick={handleGenerateAI}
              disabled={loading}
              className="flex-1 px-6 py-3 bg-gradient-to-r from-purple-600 to-blue-600 text-white font-semibold rounded-lg hover:from-purple-700 hover:to-blue-700 focus:outline-none focus:ring-2 focus:ring-purple-500 focus:ring-offset-2 disabled:opacity-50 disabled:cursor-not-allowed transition-all"
            >
              {loading ? (
                <span className="flex items-center justify-center">
                  <svg className="animate-spin -ml-1 mr-3 h-5 w-5 text-white" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24">
                    <circle className="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" strokeWidth="4"></circle>
                    <path className="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z"></path>
                  </svg>
                  Generating dengan AI...
                </span>
              ) : (
                '✨ Generate dengan AI'
              )}
            </button>
          )}

          <button
            type="submit"
            disabled={loading}
            className="flex-1 px-6 py-3 bg-blue-600 text-white font-semibold rounded-lg hover:bg-blue-700 focus:outline-none focus:ring-2 focus:ring-blue-500 focus:ring-offset-2 disabled:opacity-50 disabled:cursor-not-allowed transition-colors"
          >
            📝 Isi Manual
          </button>
        </div>

        <div className="mt-4 p-4 bg-blue-50 border border-blue-200 rounded-lg">
          <h3 className="text-sm font-semibold text-blue-900 mb-2">💡 Tips:</h3>
          <ul className="text-sm text-blue-800 space-y-1 list-disc list-inside">
            <li>Gunakan <strong>Generate dengan AI</strong> untuk auto-fill seluruh curriculum</li>
            <li>Gunakan <strong>Isi Manual</strong> untuk masuk ke form detail lengkap</li>
            <li>Durasi optimal: 4-12 minggu untuk bootcamp intensive</li>
            <li>Semakin detail konteks tambahan, semakin spesifik hasil AI</li>
          </ul>
        </div>
      </form>
    </div>
  );
};

// Example usage component with state management
export const BootcampFormContainer: React.FC = () => {
  const [loading, setLoading] = useState(false);
  const [generatedData, setGeneratedData] = useState<BootcampData | null>(null);

  const handleSubmit = (formData: BootcampFormInput) => {
    console.log('Manual form submission:', formData);
    // Navigate to detailed form or save initial data
    alert('Form submitted! Redirect to detailed editor...');
  };

  const handleGenerateAI = async (formData: BootcampFormInput) => {
    setLoading(true);
    try {
      // Call AI API
      const response = await fetch('/api/generate-bootcamp', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(formData)
      });

      if (!response.ok) {
        throw new Error('AI generation failed');
      }

      const data = await response.json();
      setGeneratedData(data);
      
      console.log('AI Generated Data:', data);
      alert('Bootcamp curriculum berhasil di-generate! Check console for data.');
      
    } catch (error) {
      console.error('Error generating with AI:', error);
      alert('Error: ' + (error instanceof Error ? error.message : 'Unknown error'));
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="min-h-screen bg-gradient-to-br from-blue-50 to-purple-50 py-12">
      <BootcampForm
        onSubmit={handleSubmit}
        onGenerateAI={handleGenerateAI}
        loading={loading}
      />

      {/* Preview Generated Data */}
      {generatedData && (
        <div className="max-w-4xl mx-auto mt-8 p-6 bg-white rounded-lg shadow-lg">
          <h2 className="text-2xl font-bold text-gray-900 mb-4">
            ✅ Generated Bootcamp Data
          </h2>
          <pre className="bg-gray-100 p-4 rounded-lg overflow-auto max-h-96 text-sm">
            {JSON.stringify(generatedData, null, 2)}
          </pre>
          <div className="mt-4 flex gap-4">
            <button className="px-6 py-2 bg-green-600 text-white rounded-lg hover:bg-green-700">
              📥 Download JSON
            </button>
            <button className="px-6 py-2 bg-blue-600 text-white rounded-lg hover:bg-blue-700">
              📄 Generate DOCX
            </button>
          </div>
        </div>
      )}
    </div>
  );
};

export default BootcampForm;
