/** @type {import('tailwindcss').Config} */
module.exports = {
    mode: 'jit',
    content: ["./templates/**/*.{html,htm,j2}"],
    theme: {
        extend: {
            container: {
                center: true,
                padding: '0.75rem',
                screens: {
                    'DEFAULT': '1024px',
                }
            }
        },
    },
    plugins: [],
  }
