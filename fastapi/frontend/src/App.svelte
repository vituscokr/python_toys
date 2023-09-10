<script>
  import Router from 'svelte-spa-router'
  import Home from './routes/home.svelte'
  import Detail from "./routes/question_detail.svelte"
  import QuestionCreate from './routes/question_create.svelte'
  import Navigation from './components/navigation.svelte'
  import UserCreate from './routes/user_create.svelte'
  import UserLogin from './routes/user_login.svelte'
  const routes = {
    '/': Home,
    '/question/:question_id': Detail,
    '/question_create' : QuestionCreate,
    '/user-create': UserCreate,
    '/user-login': UserLogin
  }
</script>

<Navigation />
<Router {routes}/>