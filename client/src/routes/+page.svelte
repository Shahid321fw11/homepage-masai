<script>
	import '../app.css';
	import Navbar from '../components/Navbar.svelte';
	import Footer from '../components/Footer.svelte';
	import News from '../components/News.svelte';
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
