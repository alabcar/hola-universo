// @ts-check
import { defineConfig } from 'astro/config';
import starlight from '@astrojs/starlight';

// https://astro.build/config
export default defineConfig({
	site: 'https://alabcar.github.io',
	base: '/hola-universo',
	integrations: [
		starlight({
			title: 'Hola, universo',
			description:
				'Plan de estudio como afición en astronomía, física y matemáticas: cada semana empieza con una pregunta del cielo.',
			defaultLocale: 'root',
			locales: {
				root: { label: 'Castellano', lang: 'es' },
			},
			sidebar: [
				{
					label: 'Empezar',
					items: [{ label: 'Cómo estudiar', slug: 'como-estudiar' }],
				},
				{
					label: 'Fase 1 · Principios básicos de astronomía',
					items: [{ autogenerate: { directory: 'fase-1' } }],
				},
				{
					label: 'Fase 2 · Órbitas',
					items: [{ autogenerate: { directory: 'fase-2' } }],
				},
				{
					label: 'Fase 3 · La luz',
					items: [{ autogenerate: { directory: 'fase-3' } }],
				},
				{
					label: 'Fase 4 · El universo grande',
					items: [{ autogenerate: { directory: 'fase-4' } }],
				},
				{ label: 'Recursos', slug: 'recursos' },
				{ label: 'Créditos y licencias', slug: 'creditos' },
			],
		}),
	],
});
