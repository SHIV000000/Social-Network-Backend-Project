module.exports = {
  content: [
      './templates/**/*.html',
      './static/**/*.css',
      './src/**/*.{js,jsx,ts,tsx}',
      './node_modules/daisyui/**/*.js',
  ],
  theme: {
      extend: {},
  },
  plugins: [
      require('daisyui'),
  ],
}
