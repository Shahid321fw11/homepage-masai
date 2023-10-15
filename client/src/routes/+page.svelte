<script>
	import '../app.css';
	import Navbar from '../components/Navbar.svelte';
	import Footer from '../components/Footer.svelte';
</script>

<slot />
<section>
	<Navbar />
</section>

<section>
	<Footer />
</section>
