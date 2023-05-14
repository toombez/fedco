/** @type {import('tailwindcss').Config} */
module.exports = {
    mode: 'jit',
    content: ["./templates/**/*.{html,htm,j2}"],
    theme: {
        colors: {
            white: '#EEEEEE',
            gray: '#00AAB8B8',
            black: '#232123',
            'light-black': '#3F313F',
            yellow: '#E7CC69',
            green: '#1B9C85',
            purple: '#9B82C2',

            services: {
                vk: '#0077FF',
                telegram: '#2BA6E1',
                github: '#000000',
                discord: '#5566E4',
                email: 'colors.yellow',
            },
        },
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
