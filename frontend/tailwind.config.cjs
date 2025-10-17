module.exports = {
  content: ['./index.html', './src/**/*.{js,jsx,ts,tsx}'],
  theme: {
    extend: {
      colors: {
        brand: {
          50: '#eef2ff',
          100: '#e0e7ff',
          300: '#a5b4fc',
          500: '#6366f1', // indigo 500
          700: '#4338ca',
        },
        slate: {
          50: '#f8fafc',
          100: '#f1f5f9',
          700: '#334155'
        },
        teal: {
          500: '#14b8a6'
        }
      }
    }
  },
  plugins: [],
}
