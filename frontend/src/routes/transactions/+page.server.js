import { error } from '@sveltejs/kit';
/** @type {import('./$types').PageServerLoad} */
export async function load() {
	const response = await fetch('http://127.0.0.1:5000/api/get_all_transactions');
	if (response.ok) {
		const data = response.json();
		console.log(data);
		return {
			transactions: data
		};
	}
	error(404, 'Not found');
}
