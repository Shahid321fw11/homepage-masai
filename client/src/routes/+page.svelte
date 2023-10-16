<script>
	import '../app.css';
	import Navbar from '../components/Navbar.svelte';
	import Footer from '../components/Footer.svelte';
	import News from '../components/News.svelte';
	import Certificate from '../components/Certificate.svelte';
	import Hero from '../components/Hero.svelte';
	import Courses from '../components/Courses.svelte';
	import Potential from '../components/Potential.svelte';
	import Elevate from '../components/Elevate.svelte';
	import Hiring from '../components/Hiring.svelte';
	// import NewNavbar from '../components/NewNavbar.svelte';
	// import Curriculum from '../components/Curriculum.svelte';
</script>

<slot />
<section>
	<Navbar />
</section>

<!-- <section>
	<NewNavbar />
</section> -->

<section>
	<Hero />
</section>

<section>
	<Potential />
</section>

<section>
	<Courses />
</section>

<!-- <section>
	<Curriculum />
</section> -->

<section>
	<Hiring />
</section>

<section>
	<Elevate />
</section>

<section>
	<Certificate />
</section>

<section>
	<News />
</section>

<section>
	<Footer />
</section>
