<script>
  import Router from 'svelte-spa-router'
  import Home from './routes/home.svelte'
  import Detail from "./routes/question_detail.svelte"
  import QuestionCreate from './routes/question_create.svelte'
  import Navigation from './components/navigation.svelte'
  import UserCreate from './routes/user_create.svelte'
  import UserLogin from './routes/user_login.svelte'
  import QuestionModify from './routes/question_modify.svelte'
  import AnswerModify from './routes/answer_modify.svelte'
  const routes = {
    '/': Home,
    '/question/:question_id': Detail,
    '/question_create' : QuestionCreate,
    '/user-create': UserCreate,
    '/user-login': UserLogin,
    '/question-modify/:question_id': QuestionModify,
    '/answer-modify/:answer_id': AnswerModify 
  }
</script>

<Navigation />
<Router {routes}/>