import { defineConfig } from 'tsup'

export default defineConfig({
    minify: true,
    clean: true,
    format: ['cjs'],
    outDir: './web/static/js/',
})
