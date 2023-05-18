import { Config } from 'tailwindcss'
import defaultTheme from 'tailwindcss/defaultTheme'

export default {
    mode: 'jit',
    content: ["./web/templates/**/*.{html,htm,j2}"],
    theme: {
        fontFamily: {
            headings: ['Montserrat', ...defaultTheme.fontFamily.sans],
            regular: ['Raleway', ...defaultTheme.fontFamily.mono],
        },
        colors: {
            transparent: 'transparent',
            white: '#EEEEEE',
            gray: '#ABB9B9',
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
        screens: {
            'mobile': '640px',
            'desktop': '1024px',
        },
        container: {
            center: true,
            padding: {
                mobile: '0.5rem',
                desktop: '0.75rem',
            },
        },
    },
    plugins: [],
} as Config
