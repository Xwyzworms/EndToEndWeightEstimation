package com.TA.myapplication

import android.os.Bundle
import android.util.Log
import androidx.fragment.app.Fragment
import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup
import androidx.lifecycle.ViewModelProvider
import com.TA.myapplication.databinding.FragmentHomeBinding
import com.TA.myapplication.ui.HomeFragmentViewModel
import com.TA.myapplication.utility.ViewModelFactory
import com.google.firebase.database.DataSnapshot
import com.google.firebase.database.DatabaseError
import com.google.firebase.database.DatabaseReference
import com.google.firebase.database.ValueEventListener


class HomeFragment : Fragment() {
    private var _binding : FragmentHomeBinding? = null
    private val binding get() = _binding!!

    private lateinit var factory : ViewModelFactory
    private lateinit var homeViewModel  : HomeFragmentViewModel

    private var dataPath : String = "data"


    override fun onViewCreated(view: View, savedInstanceState: Bundle?) {
        super.onViewCreated(view, savedInstanceState)
        factory = ViewModelFactory.getInstance()
        homeViewModel = ViewModelProvider(this, factory)[HomeFragmentViewModel::class.java]
        val dataJson : DatabaseReference? = homeViewModel.getTheJson(dataPath)
        Log.d(TAG, dataJson.toString())
        if (dataJson != null) {
            dataJson.addListenerForSingleValueEvent(object : ValueEventListener {
                override fun onDataChange(snapshot: DataSnapshot) {
                    Log.d(TAG, snapshot.value.toString())
                }

                override fun onCancelled(error: DatabaseError) {
                    Log.d(TAG,"Error Here ${error.message.toString()}")
                }

            })
        }
        else {
            Log.d(TAG, "NO DATA !!")
        }
    }

    override fun onCreateView(
        inflater: LayoutInflater, container: ViewGroup?,
        savedInstanceState: Bundle?
    ): View {
        _binding = FragmentHomeBinding.inflate(inflater, container, false)
        return binding.root
    }

    companion object {
        private val TAG :String = HomeFragment::class.java.simpleName
    }


}