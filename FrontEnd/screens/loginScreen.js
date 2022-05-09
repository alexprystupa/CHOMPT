import React, { useState } from 'react';
import { View, StyleSheet, TouchableOpacity, Text, Image, Button, TextInput } from 'react-native';


const LoginScreen = ({ navigation }) => {
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  return (
    <View style = {styles.container}>
      <Image style={styles.image} source = {require('../assets/icons/bread.png')}/>
      <View style={styles.inputView}>
        <TextInput
          style={styles.TextInput}
          textAlign={'center'}
          placeholder="Email"
          placeholderTextColor="#003f5c"
          onChangeText={(email) => setEmail(email)}
          />
      </View>

      <View style={styles.inputView}>
        <TextInput
          style={styles.TextInput}
          textAlign={'center'}
          placeholder="Password"
          placeholderTextColor="#003f5c"
          secureTextEntry={true}
          onChangeText={(password) => setPassword(password)}
        />
      </View>

      <TouchableOpacity>
        <Text style={styles.forgotButton}>Forgot Password?</Text>
      </TouchableOpacity>

      <TouchableOpacity style={styles.loginBtn}>
        <Text 
          style={styles.loginText}
          onPress={() => navigation.navigate("MapScreen")}
        >LOGIN
        </Text>
      </TouchableOpacity>
    </View>
  )
}

const styles = StyleSheet.create({
  mainContainer: {
    flex: 1,
    paddingTop: 60,
  },
  container: {
    flex: 1,
    backgroundColor: '#fff',
    alignItems: 'center',
    justifyContent: 'center',
  },
  image: {
    marginBottom: 40,
    width: 80,
    height: 80,
  },
  inputView: {
    backgroundColor: '#ffc299',
    borderRadius: 30,
    width: "70%",
    height: 45,
    marginBottom: 20,
    alignItems: "center",
    justifyContent: "center",
    textAlign: "center",
  },
  TextInput: {
    height: 50,
    flex: 1,
    padding: 10,
    marginLeft: 20,
    textAlign: "center",
  },
  forgotPassword: {
    height: 30,
    marginBottom: 30,
  },
  loginBtn: {
    width: '80%',
    borderRadius: 25,
    height: 50,
    alignItems: 'center',
    justifyContent: 'center',
    marginTop: 40,
    backgroundColor:"#ff8533",
  }
})

export default LoginScreen;