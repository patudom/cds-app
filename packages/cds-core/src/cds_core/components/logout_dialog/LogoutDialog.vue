<template>
  <div class="text-center">
    <v-dialog
      v-model="this.dialog"
      persistent
      width="500"
    >
      <v-card>
        <v-card-title class="text-h5">
          Not Logged In
        </v-card-title>

        <v-card-text>
          You must be logged in to access this story. Return to the Portal and log in with your credentials.
        </v-card-text>

        <v-divider></v-divider>

        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn
            color="primary"
            text
            :href="this.return_url"
          >
            Return
          </v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>
  </div>
</template>

<style scoped>

</style>

<script>
  export default {
    name: "LogoutDialog",
  }
</script>