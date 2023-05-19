import { Config } from 'tailwindcss'
import defaultTheme from 'tailwindcss/defaultTheme'

export default {
    mode: 'jit',
    content: ["./web/templates/**/*.{html,htm,j2}"],
    theme: {
        fontSize: {
            md: '0.875rem',
            '2md': '1rem',
            lg: '1.5rem',
            '2lg': '1.75rem',
            xl: '2.25rem',
            '2xl': '2.5rem',

        },
        fontFamily: {
            montserrat: ['Montserrat', ...defaultTheme.fontFamily.sans],
            raleway: ['Raleway', ...defaultTheme.fontFamily.mono],
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
        },
    },
    plugins: [],
} as Config
