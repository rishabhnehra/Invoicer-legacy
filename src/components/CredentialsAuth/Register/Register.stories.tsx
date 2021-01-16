import {Story, Meta} from '@storybook/react/types-6-0';

import { Register as RegisterComponent } from '../index';

export default {
    title: 'Components/Credentials Auth',
    component: RegisterComponent
} as Meta;

const Template: Story = () => <RegisterComponent />

export const Register = Template.bind({});