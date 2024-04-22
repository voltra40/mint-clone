<script>
	import {onMount} from "svelte"
	let isLoading = false
	let totals = {}

	onMount(async () => {
		const response = await fetch("http://127.0.0.1:5000/api/totals")
		if (response.ok) {
			totals = await response.json()
		}
	})
</script>

<div>
	<h2>Totals</h2>
	{#if Object.keys(totals).length > 0}
		<ul>
			{#each Object.entries(totals) as [category, total]}
				<li>{category}: {total}</li>
			{/each}
		</ul>
	{:else}
		<p>Loading...</p>
	{/if}
</div>
