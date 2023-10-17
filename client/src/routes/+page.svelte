<script>
	import '../app.css';
	import '../non-critical-style.9657d852.css';
	import '../_layout.896888ea.css';
	import Navbar from '../components/Navbar.svelte';
	import Footer from '../components/Footer.svelte';
	import News from '../components/News.svelte';
	import Certificate from '../components/Certificate.svelte';
	import Hero from '../components/Hero.svelte';
	import Courses from '../components/Courses.svelte';
	import Potential from '../components/Potential.svelte';
	import Elevate from '../components/Elevate.svelte';
	import Hiring from '../components/Hiring.svelte';
	// import Community from '../components/Community.svelte';
	import Curriculum from '../components/Curriculum.svelte';
	import Outcomes from '../components/Outcomes.svelte';
	// import Impact from '../components/Impact.svelte';
	// import ImpactNew from '../components/ImpactNew.svelte';
</script>

<slot />
<section class="fixed w-full z-[500]">
	<Navbar />
</section>
<section class="h-[144px]" />

<section>
	<Hero />
</section>

<section>
	<Potential />
</section>

<section>
	<Outcomes />
</section>

<section>
	<Courses />
</section>

<!-- <section>
	<Community />
</section> -->
<section>
	<Curriculum />
</section>

<section>
	<Hiring />
</section>

<!-- <section>
	<Impact />
</section> -->
<!-- <section>
	<ImpactNew />
</section> -->

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
