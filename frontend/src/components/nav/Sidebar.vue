<template>
  <v-navigation-drawer app clipped permanent mini-variant expand-on-hover>
    <!-- -->

    <v-list nav dense>
      <div v-for="(link, i) in links" :key="i">
        <v-list-item v-if="!link.subLinks" :to="link.to" exact class="mt-1">
          <v-list-item-icon>
            <v-icon>{{ link.icon }}</v-icon>
          </v-list-item-icon>

          <v-list-item-title v-text="link.text" />
        </v-list-item>

        <v-list-group
          v-else
          :key="link.text"
          :prepend-icon="link.icon"
          :value="false"
        >
          <template v-slot:activator>
            <v-list-item-title>{{ link.text }}</v-list-item-title>
          </template>

          <v-list-item
            v-for="sublink in link.subLinks"
            :to="sublink.to"
            :key="sublink.text"
            exact
            class="mb-1"
          >
            <v-list-item-icon>
              <v-icon>{{ sublink.icon }}</v-icon>
            </v-list-item-icon>
            <v-list-item-title>{{ sublink.text }}</v-list-item-title>
          </v-list-item>
        </v-list-group>
        <v-divider />
      </div>
    </v-list>
    <template v-slot:append>
      <a :href="'https://' + 'github.com/SelfhostedPro/Yacht'">
        <v-icon size="200%" class="pa-2">mdi-github</v-icon>
      </a>
    </template>
  </v-navigation-drawer>
</template>

<script>
export default {
  data: () => ({
    links: [
      {
        to: "/",
        icon: "mdi-view-dashboard",
        text: "Dashboard",
        divider: true,
      },
      {
        icon: "mdi-application",
        text: "Applications",
        subLinks: [
          {
            text: "View Applications",
            to: "/apps",
            icon: "mdi-view-list",
          },
          {
            text: "New Application",
            to: "/apps/deploy",
            icon: "mdi-plus",
          },
        ],
      },
      {
        icon: "mdi-folder",
        text: "Templates",
        subLinks: [
          {
            text: "View Templates",
            to: "/templates",
            icon: "mdi-view-list",
          },
          {
            text: "New Template",
            to: "/templates/new",
            icon: "mdi-plus",
          },
        ],
      },
      {
        to: "/settings/info",
        icon: "mdi-cog",
        text: "Settings",
      },
      {
        icon: "mdi-book-open-outline",
        text: "Compose",
        subLinks: [
          {
            text: "Compose List",
            to: "/compose",
            icon: "mdi-format-list-bulleted"
          },
          {
            text: "New Compose",
            to: "/compose/edit",
            icon: "mdi-file-edit-outline"
          },
          {
            text: "Download Compose",
            to: "/compose/dl",
            icon: "mdi-file-download-outline"
          }
        ]
      }
    ],
  }),
};
</script>

<style scoped>
.v-application--is-ltr
  .v-list--dense.v-list--nav
  .v-list-group--no-action
  > .v-list-group__items
  > .v-list-item {
  padding: 0 8px;
}
</style>
