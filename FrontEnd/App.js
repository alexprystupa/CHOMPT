import React, { useState } from 'react';
import LoginScreen from './screens/loginScreen'
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
          name = "LoginScreen"
          component = { LoginScreen }
        />
        <Stack.Screen
        name = "SocialScreen"
        component = { Tabs }
        options={{title: "Form Quiz Section"}}
        />
        <Stack.Screen
        name = "MapScreen"
        component = { Tabs }
        />
      </Stack.Navigator>
    </NavigationContainer>
  )
}

export default App;
