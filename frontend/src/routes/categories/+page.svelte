<script>
	/** @type {import('./$types').PageData} */
	export let data;
</script>

<svelte:head>
	<title>Categories</title>
	<meta name="description" content="All budget categories" />
</svelte:head>

<div class="container">
	<h1>Categories</h1>

	{#await data.categories}
		Loading categories...
	{:then categories}
		{#if categories.length > 0}
			<ul>
				{#each categories as category}
					<li>{category[1]}</li>
				{/each}
			</ul>
		{:else}
			<p>No categories found.</p>
		{/if}
	{:catch error}
		<p>error loading categories: {error.message}</p>
	{/await}
</div>

<style>
	.container {
		display: flex;
		flex-direction: column;
	}
	.container h1 {
		margin-bottom: 1rem;
	}
	.container ul {
		list-style-type: none;
		padding: 0;
	}
	.container li {
		padding: 0.5rem;
		border: 1px solid #ccc;
		border-radius: 0.25rem;
		margin-bottom: 0.5rem;
	}
	.container li:hover {
		background-color: #f9f9f9;
		cursor: pointer;
	}
</style>
