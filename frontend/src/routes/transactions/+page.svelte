<script>
	/** @type {import('./$types').PageData} */
	export let data;
</script>

<svelte:head>
	<title>Transactions</title>
	<meta name="description" content="All transaction data" />
</svelte:head>

<div class="container">
	<h1>Transactions</h1>

	{#await data.transactions}
		Loading transactions...
	{:then transactions}
		{#if transactions.length > 0}
			<ul>
				{#each transactions as transaction}
					<li>
						<div class="transaction-container">
							<div class="transaction-container-left">
								<div class="date">
									<p>{transaction[2]}</p>
								</div>
								<div class="details">
									<p class="description">{transaction[4]}</p>
									<p class="category">{transaction[5]}</p>
								</div>
							</div>
							<div class="transaction-container-right">
								<p>${transaction[7]}</p>
							</div>
						</div>
					</li>
				{/each}
			</ul>
		{:else}
			<p>No transactions found.</p>
		{/if}
	{:catch error}
		<p>error loading transactions: {error.message}</p>
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
		display: flex;
		flex-direction: column;
		justify-content: space-between;
		padding: 0.5rem;
		border: 1px solid #ccc;
		border-radius: 0.25rem;
		margin-bottom: 0.5rem;
	}

	.container li:hover {
		background-color: #f9f9f9;
	}

	.transaction-container {
		display: flex;
		justify-content: space-between;
		padding: 1rem;
	}

	.transaction-container-left {
		display: flex;
		flex-direction: column;
	}

	.transaction-container-left div {
		margin: 0.5rem;
	}

	.date p {
		margin: 0;
		font-size: large;
		color: #667;
	}

	.details {
		display: flex;
		flex-direction: column;
	}

	.details p {
		margin: 0;
	}

	.category {
		color: #667;
	}

	.description {
		font-weight: bold;
	}

	.transaction-container-right {
		display: flex;
		flex-direction: column;
		justify-content: center;
		margin-left: 1rem;
		margin-right: 1rem;
	}

	.transaction-container-right p {
		margin: 0;
		font-size: large;
		font-weight: bold;
	}

	@media (max-width: 768px) {
		.transaction-container {
			flex-direction: column;
		}

		.transaction-container-left {
			margin-bottom: 1rem;
		}

		.transaction-container-right {
			margin-left: 0;
			margin-right: 0;
		}

		.transaction-container-right p {
			text-align: right;
		}
	}
</style>
