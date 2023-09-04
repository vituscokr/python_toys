<script>
  import Router from 'svelte-spa-router'
  import Home from './routes/home.svelte'
  import QuestionDetail from "./routes/question_detail.svelte"
  const routes = {
    '/': Home,
    '/question/:question_id': QuestionDetail
  }
</script>

<Router {routes}/>