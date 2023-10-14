<script>
	import '../app.css';
	import Navbar from './Navbar.svelte';
	import Footer from './Footer.svelte';
</script>

<slot />

<section>
	<Navbar />
</section>

<section>
	<Footer />
</section>

<!-- <h1 class="text-3xl">Welcome to SvelteKit</h1>
<p>Visit <a href="https://kit.svelte.dev">kit.svelte.dev</a> to read the documentation</p> -->
