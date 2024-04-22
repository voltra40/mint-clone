<script>
	import {onMount} from "svelte"
	let category = ""
	let isLoading = false
	let totalSpentByCategory = null
	let totals = {}

	async function fetchByCategory() {
		isLoading = true
		const response = await fetch(
			`http://127.0.0.1:5000/api/total_spent?category=${category}`
		)
		if (response.ok) {
			const data = await response.json()
			totalSpentByCategory = data.total_spent
		} else {
			console.error("Failed to fetch total spent")
		}
		isLoading = false
	}

	onMount(async () => {})
</script>

<div>
	<input type="text" bind:value={category} placeholder="Enter category" />
	<button on:click={fetchByCategory} disabled={category === "" || isLoading}>
		Fetch Total
	</button>

	{#if totalSpentByCategory !== null}
		<h2>Total Spent in {category}</h2>
		<p>${totalSpentByCategory}</p>
	{:else if isLoading}
		<p>Loading...</p>
	{/if}
</div>
