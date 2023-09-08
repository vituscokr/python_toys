<script>
  import Router from 'svelte-spa-router'
  import Home from './routes/home.svelte'
  import Detail from "./routes/question_detail.svelte"
  import QuestionCreate from './routes/question_create.svelte';
  const routes = {
    '/': Home,
    '/question/:question_id': Detail,
    '/question_create' : QuestionCreate
  }
</script>

<Router {routes}/>