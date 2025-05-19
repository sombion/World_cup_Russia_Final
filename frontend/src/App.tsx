import { useEffect } from 'react'
import { AppRouter } from './AppRouter'
import { observer } from 'mobx-react-lite'
import { authStore } from './stores/authStore'

const App = observer(() => {
  useEffect(() => {
    authStore.loadUser();
  }, []);

  return (
   <div className='app'>
      <AppRouter/>
   </div>
  )
});

export default App
