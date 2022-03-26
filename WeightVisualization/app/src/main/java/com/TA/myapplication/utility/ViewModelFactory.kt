package com.TA.myapplication.utility

import androidx.lifecycle.ViewModel
import androidx.lifecycle.ViewModelProvider
import com.TA.myapplication.repository.DataRepository
import com.TA.myapplication.ui.HomeFragmentViewModel
import com.google.firebase.database.DatabaseReference

class ViewModelFactory(private  val dataRepository: DataRepository) : ViewModelProvider.NewInstanceFactory(){

    override fun <T : ViewModel> create(modelClass: Class<T>): T {
        when {
            modelClass.isAssignableFrom(HomeFragmentViewModel::class.java) -> {
                return HomeFragmentViewModel(dataRepository) as T
            }
        }
        throw IllegalArgumentException("Incorrect Class ${modelClass.simpleName}")
    }

    companion object {

        @Volatile
        private var INSTANCE : ViewModelFactory ? = null

        @JvmStatic
        fun getInstance() : ViewModelFactory{
            return INSTANCE ?: synchronized(this) {
                val instance = ViewModelFactory(Injection.provideRepository())
                INSTANCE = instance
                instance
            }
        }
    }

}