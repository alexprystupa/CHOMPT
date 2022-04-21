import React from 'react';
import ProfileScreen from './screens/profileScreen'
import MapScreen from './screens/mapScreen';
import SocialScreen from './screens/socialScreen';
import { NavigationContainer } from '@react-navigation/native';
import { createNativeStackNavigator } from '@react-navigation/native-stack';
import Tabs from './components/Tabs'

const Stack = createNativeStackNavigator();

const App = () => {
  return(
    <NavigationContainer>
      <Stack.Navigator
        screenOptions={{
          headerShown: false
        }}
      >
        <Stack.Screen
          name = "ProfileScreen"
          component = { ProfileScreen, Tabs }
        />
        <Stack.Screen
          name = "MapScreen"
          component = { MapScreen, Tabs }
        />
        <Stack.Screen
        name = "SocialScreen"
        component = { SocialScreen }
        options={{title: "Form Quiz Section", presentation: "modal"}}
        />
      </Stack.Navigator>
    </NavigationContainer>
  )
}

export default App;
